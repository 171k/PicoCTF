#!/usr/bin/env python3
import sys
import binascii

def swap_endian(hex_str, chunk_size):
    """
    Convert hex string from little endian to big endian by
    reversing bytes within each chunk.
    """
    if len(hex_str) % 2 != 0:
        raise ValueError("Hex string length must be even")

    bytes_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]

    # Group bytes by chunk_size (in bytes)
    chunks = [bytes_list[i:i+chunk_size] for i in range(0, len(bytes_list), chunk_size)]

    # Reverse each chunk (little ↔ big endian)
    swapped = ["".join(reversed(chunk)) for chunk in chunks]
    return "".join(swapped)


def file_to_hex(filename):
    with open(filename, "rb") as f:
        return binascii.hexlify(f.read()).decode()


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 hex_little_to_big.py <input_file> <chunk_size>")
        print("Example: python3 hex_little_to_big.py data.bin 4")
        sys.exit(1)

    input_file = sys.argv[1]
    chunk_size = int(sys.argv[2])

    hex_data = file_to_hex(input_file)
    converted = swap_endian(hex_data, chunk_size)

    out_file = input_file + ".bigend"
    with open(out_file, "wb") as f:
        f.write(binascii.unhexlify(converted))

    print(f"[+] Converted file written to: {out_file}")


if __name__ == "__main__":
    main()
