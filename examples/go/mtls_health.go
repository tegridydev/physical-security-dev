// Read one health endpoint using mutual TLS and an explicit client certificate.
package main

import (
	"bytes"
	"crypto/tls"
	"crypto/x509"
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"io"
	"mime"
	"net/http"
	"net/url"
	"os"
	"strings"
	"time"
)

const maxBytes = 65536

type Health struct {
	Status string `json:"status"`
}

func parseHealth(data []byte) (Health, error) {
	if len(data) > maxBytes {
		return Health{}, errors.New("response exceeds 64 KiB")
	}
	decoder := json.NewDecoder(bytes.NewReader(data))
	token, err := decoder.Token()
	if err != nil || token != json.Delim('{') {
		return Health{}, errors.New("expected an object")
	}
	seen := false
	result := Health{}
	for decoder.More() {
		key, err := decoder.Token()
		if err != nil || key != "status" || seen {
			return Health{}, errors.New("unknown or duplicate field")
		}
		seen = true
		if err := decoder.Decode(&result.Status); err != nil {
			return Health{}, err
		}
	}
	if _, err := decoder.Token(); err != nil {
		return Health{}, err
	}
	if _, err := decoder.Token(); err != io.EOF {
		return Health{}, errors.New("trailing JSON data")
	}
	if !seen || (result.Status != "healthy" && result.Status != "degraded") {
		return Health{}, errors.New("expected status healthy or degraded")
	}
	return result, nil
}

func readHealth(endpoint, caFile, certFile, keyFile string) (Health, error) {
	target, err := url.Parse(endpoint)
	if err != nil || target.Scheme != "https" || target.Hostname() == "" || target.User != nil || target.Fragment != "" {
		return Health{}, errors.New("use an HTTPS URL without embedded credentials")
	}
	if certFile == "" || keyFile == "" {
		return Health{}, errors.New("client certificate and key are required")
	}
	certificate, err := tls.LoadX509KeyPair(certFile, keyFile)
	if err != nil {
		return Health{}, errors.New("cannot load the client certificate and key")
	}
	roots, err := x509.SystemCertPool()
	if err != nil || roots == nil {
		roots = x509.NewCertPool()
	}
	if caFile != "" {
		pem, err := os.ReadFile(caFile)
		if err != nil || !roots.AppendCertsFromPEM(pem) {
			return Health{}, errors.New("cannot load the CA bundle")
		}
	}
	transport := &http.Transport{
		Proxy: nil,
		TLSClientConfig: &tls.Config{MinVersion: tls.VersionTLS12, RootCAs: roots,
			Certificates: []tls.Certificate{certificate}},
		TLSHandshakeTimeout:    5 * time.Second,
		ResponseHeaderTimeout:  5 * time.Second,
		MaxResponseHeaderBytes: 16384,
		DisableCompression:     true,
	}
	defer transport.CloseIdleConnections()
	client := &http.Client{Transport: transport, Timeout: 15 * time.Second,
		CheckRedirect: func(req *http.Request, via []*http.Request) error { return http.ErrUseLastResponse }}
	request, err := http.NewRequest(http.MethodGet, target.String(), nil)
	if err != nil {
		return Health{}, err
	}
	request.Header.Set("Accept", "application/json")
	request.Header.Set("Accept-Encoding", "identity")
	response, err := client.Do(request)
	if err != nil {
		return Health{}, errors.New("connection or certificate validation failed")
	}
	defer response.Body.Close()
	if response.StatusCode != http.StatusOK {
		return Health{}, fmt.Errorf("unexpected HTTP status %d", response.StatusCode)
	}
	media, _, err := mime.ParseMediaType(response.Header.Get("Content-Type"))
	if err != nil || media != "application/json" {
		return Health{}, errors.New("expected application/json")
	}
	encoding := strings.ToLower(response.Header.Get("Content-Encoding"))
	if encoding != "" && encoding != "identity" {
		return Health{}, errors.New("compressed responses are not accepted")
	}
	data, err := io.ReadAll(io.LimitReader(response.Body, maxBytes+1))
	if err != nil {
		return Health{}, err
	}
	return parseHealth(data)
}

func main() {
	demo := flag.Bool("demo", false, "validate a built in response without networking")
	endpoint := flag.String("url", "", "exact HTTPS health endpoint")
	ca := flag.String("ca", "", "optional private CA PEM file")
	cert := flag.String("cert", "", "client certificate PEM file")
	key := flag.String("key", "", "client private key PEM file")
	flag.Parse()
	var result Health
	var err error
	if flag.NArg() != 0 || (*demo && *endpoint != "") || (!*demo && *endpoint == "") {
		fmt.Fprintln(os.Stderr, "Use --demo or --url with --cert and --key")
		os.Exit(2)
	}
	if *demo {
		result, err = parseHealth([]byte(`{"status":"healthy"}`))
	} else {
		result, err = readHealth(*endpoint, *ca, *cert, *key)
	}
	if err != nil {
		fmt.Fprintln(os.Stderr, "Error:", err)
		os.Exit(1)
	}
	if err := json.NewEncoder(os.Stdout).Encode(result); err != nil {
		os.Exit(1)
	}
}
