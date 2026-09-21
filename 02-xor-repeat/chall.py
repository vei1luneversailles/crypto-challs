#!/usr/bin/env python3
"""
XORientation
Flag di-XOR dengan key pendek (repeating key XOR).
"""

FLAG = open("flag.txt", "rb").read().strip()
KEY = open("key.txt", "rb").read().strip()  # dirahasiakan, panjang <= 4 byte

def xor_repeat(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

if __name__ == "__main__":
    ct = xor_repeat(FLAG, KEY)
    print(ct.hex())
