---
title: "Mutual-TLS health client in Go"
summary: "A read-only Go HTTPS health request with explicit client identity, trust, timeouts, and body bounds."
page_type: development
domains:
  - development
tags:
  - go
  - mtls
coverage_limit: "Read-only reference client using a reserved documentation domain; certificate policy, endpoint authorization, Go patch level, and product behavior are environment-specific."
languages:
  - Go
scope: global
content_status: maintained
technology_status: current
verification: V2
runtime_status: not-executed
safety_level: safety-relevant
standards:
  - "Go 1.27"
  - "TLS 1.3, RFC 8446"
  - "RFC 9325 / BCP 195"
created: 2026-08-25
last_updated: 2026-08-25
last_verified: 2026-08-25
next_review: 2026-11-23
---

# Mutual-TLS health client in Go

[Home](../../README.md) / [Development](../README.md) / [Examples](README.md) / mTLS health client

Target: Go 1.27, standard library only  
Target name: device.example, reserved for documentation  
Network behavior: one read-only GET after an integration owner configures an isolated authorized endpoint

## Complete example

~~~go
package main

import (
	"bytes"
	"context"
	"crypto/tls"
	"crypto/x509"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"mime"
	"net/http"
	"os"
	"time"
)

const (
	maxBody            = 64 * 1024
	maxResponseHeaders = 16 * 1024
)

type healthResponse struct {
	Status string `json:"status"`
}

func main() {
	if len(os.Args) != 4 {
		fmt.Fprintln(os.Stderr, "usage: mtls-health CLIENT_CERT CLIENT_KEY ROOT_CA")
		os.Exit(2)
	}

	clientCert, err := tls.LoadX509KeyPair(os.Args[1], os.Args[2])
	if err != nil {
		fatal("load client identity", err)
	}
	rootPEM, err := os.ReadFile(os.Args[3])
	if err != nil {
		fatal("read root CA", err)
	}
	roots := x509.NewCertPool()
	if !roots.AppendCertsFromPEM(rootPEM) {
		fatal("parse root CA", errors.New("no certificate found"))
	}

	transport := &http.Transport{
		TLSClientConfig: &tls.Config{
			MinVersion:   tls.VersionTLS12,
			ServerName:   "device.example",
			RootCAs:      roots,
			Certificates: []tls.Certificate{clientCert},
		},
		ResponseHeaderTimeout:  3 * time.Second,
		IdleConnTimeout:        15 * time.Second,
		MaxResponseHeaderBytes: maxResponseHeaders,
	}
	defer transport.CloseIdleConnections()
	client := &http.Client{
		Transport: transport,
		Timeout:   5 * time.Second,
		CheckRedirect: func(_ *http.Request, _ []*http.Request) error {
			return errors.New("redirects disabled")
		},
	}

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	req, err := http.NewRequestWithContext(ctx, http.MethodGet,
		"https://device.example/api/v1/health", nil)
	if err != nil {
		fatal("create request", err)
	}
	req.Header.Set("Accept", "application/json")

	resp, err := client.Do(req)
	if err != nil {
		fatal("request", err)
	}
	defer resp.Body.Close()
	if resp.StatusCode != http.StatusOK {
		fatal("status", fmt.Errorf("unexpected HTTP status %d", resp.StatusCode))
	}
	mediaType, _, err := mime.ParseMediaType(resp.Header.Get("Content-Type"))
	if err != nil || mediaType != "application/json" {
		fatal("content type", errors.New("expected application/json"))
	}

	limited := io.LimitReader(resp.Body, maxBody+1)
	body, err := io.ReadAll(limited)
	if err != nil {
		fatal("read response", err)
	}
	if len(body) > maxBody {
		fatal("read response", errors.New("body exceeds configured limit"))
	}
	decoded, err := decodeHealth(body)
	if err != nil {
		fatal("decode response", err)
	}
	if decoded.Status != "healthy" && decoded.Status != "degraded" {
		fatal("validate response", errors.New("unknown status"))
	}
	fmt.Println("validated health state:", decoded.Status)
}

func decodeHealth(body []byte) (healthResponse, error) {
	decoder := json.NewDecoder(bytes.NewReader(body))
	start, err := decoder.Token()
	if err != nil {
		return healthResponse{}, err
	}
	startDelimiter, ok := start.(json.Delim)
	if !ok || startDelimiter != '{' {
		return healthResponse{}, errors.New("response must be a JSON object")
	}

	var decoded healthResponse
	seenStatus := false
	for decoder.More() {
		keyToken, err := decoder.Token()
		if err != nil {
			return healthResponse{}, err
		}
		key, ok := keyToken.(string)
		if !ok || key != "status" {
			return healthResponse{}, errors.New("unexpected response member")
		}
		if seenStatus {
			return healthResponse{}, errors.New("duplicate status member")
		}
		if err := decoder.Decode(&decoded.Status); err != nil {
			return healthResponse{}, err
		}
		seenStatus = true
	}

	end, err := decoder.Token()
	if err != nil {
		return healthResponse{}, err
	}
	endDelimiter, ok := end.(json.Delim)
	if !ok || endDelimiter != '}' || !seenStatus {
		return healthResponse{}, errors.New("invalid response object")
	}
	if err := decoder.Decode(&struct{}{}); err != io.EOF {
		return healthResponse{}, errors.New("trailing JSON content")
	}
	return decoded, nil
}

func fatal(operation string, err error) {
	fmt.Fprintln(os.Stderr, operation+":", err)
	os.Exit(1)
}
~~~

## Limits

The example loads a deployment-supplied client key from disk for clarity; a production design may require OS, hardware, or workload-identity storage. TLS 1.2 is the minimum here for device compatibility, not a universal recommendation; prefer TLS 1.3 where the product profile supports it and apply RFC 9325 to any TLS 1.2 profile. The integration owner must choose policy from exact product support and current requirements. Response headers and body are bounded. The response parser requires `application/json`, one `status` member, no unknown or duplicate members, and no trailing JSON value.

## Environment validation checklist

- [ ] Cover success, wrong server name, untrusted CA, and expired or denied client identity against an isolated authorized endpoint.
- [ ] Cover connection/response timeout, redirect denial, oversized response, wrong HTTP status/content type, malformed JSON, duplicate/unknown members, and trailing JSON.
- [ ] Confirm client-key file permissions, trust-store provenance, certificate rollover, and log redaction.
- [ ] Record Go/OS versions, endpoint implementation, certificate profile, cases, observations, and limitations.

## Sources

- [Go crypto/tls](https://pkg.go.dev/crypto/tls), accessed 2026-08-25.
- [Go net/http](https://pkg.go.dev/net/http), accessed 2026-08-25.
- [RFC 8446 TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446), accessed 2026-08-25.
- [RFC 9325 / BCP 195: Recommendations for Secure Use of TLS and DTLS](https://www.rfc-editor.org/info/rfc9325/), accessed 2026-08-25.

## Related pages

- [Go guide](../language-guides/go.md)
- [PKI, certificates, keys, and secrets](../../06-security-and-assurance/pki-certificates-keys-and-secrets.md)
