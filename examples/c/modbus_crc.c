/* Inspect a captured Modbus RTU read response. No serial or network access. */
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

static uint16_t crc16(const uint8_t *data, size_t length) {
    uint16_t crc = 0xFFFFu;
    for (size_t i = 0; i < length; ++i) {
        crc ^= data[i];
        for (unsigned bit = 0; bit < 8; ++bit) {
            crc = (uint16_t)((crc >> 1) ^ ((crc & 1u) ? 0xA001u : 0u));
        }
    }
    return crc;
}

static bool valid_frame(const uint8_t *frame, size_t length) {
    if (length < 7 || length > 255 || frame[0] < 1 || frame[0] > 247) return false;
    if ((frame[1] != 3 && frame[1] != 4) || frame[2] < 2 || frame[2] > 250 || frame[2] % 2 != 0) return false;
    if ((size_t)frame[2] + 5 != length) return false;
    const uint16_t received = (uint16_t)((uint16_t)frame[length - 2] | ((uint16_t)frame[length - 1] << 8));
    return crc16(frame, length - 2) == received;
}

static int nibble(unsigned char ch) {
    if (ch >= '0' && ch <= '9') return ch - '0';
    if (ch >= 'a' && ch <= 'f') return ch - 'a' + 10;
    if (ch >= 'A' && ch <= 'F') return ch - 'A' + 10;
    return -1;
}

static bool parse_hex(const char *text, uint8_t *output, size_t *length) {
    if (strlen(text) > 1024) return false;
    size_t count = 0;
    int high = -1;
    for (const unsigned char *p = (const unsigned char *)text; *p != 0; ++p) {
        if (isspace(*p)) { if (high >= 0) return false; continue; }
        int value = nibble(*p);
        if (value < 0) return false;
        if (high < 0) { high = value; continue; }
        if (count >= 256) return false;
        output[count++] = (uint8_t)(high * 16 + value);
        high = -1;
    }
    *length = count;
    return high < 0 && count > 0;
}

int main(int argc, char **argv) {
    uint8_t frame[256] = {1, 3, 4, 0, 10, 0, 20, 0, 0};
    size_t length = 9;
    const uint16_t checksum = crc16(frame, 7);
    frame[7] = (uint8_t)checksum;
    frame[8] = (uint8_t)(checksum >> 8);
    if (argc == 2 && strcmp(argv[1], "--self-test") == 0) {
        const uint8_t vector[] = "123456789";
        if (crc16(vector, 9) != 0x4B37u || !valid_frame(frame, length) || valid_frame(frame, 3)) return 1;
        frame[4] ^= 1u;
        if (valid_frame(frame, length)) return 1;
        puts("CRC and frame tests passed");
        return 0;
    }
    if (argc == 3 && strcmp(argv[1], "--hex") == 0) {
        if (!parse_hex(argv[2], frame, &length)) { fputs("Error: invalid hex input\n", stderr); return 1; }
    } else if (argc != 2 || strcmp(argv[1], "--demo") != 0) {
        fputs("Usage: modbus_crc --demo | --self-test | --hex \"01 03 ...\"\n", stderr);
        return 2;
    }
    if (!valid_frame(frame, length)) { fputs("Error: invalid read response or CRC\n", stderr); return 1; }
    printf("{\"unit\":%u,\"function\":%u,\"registers\":[", (unsigned)frame[0], (unsigned)frame[1]);
    for (size_t index = 0; index < frame[2]; index += 2) {
        unsigned value = (unsigned)frame[index + 3] * 256u + frame[index + 4];
        printf("%s%u", index ? "," : "", value);
    }
    puts("]}");
    return 0;
}
