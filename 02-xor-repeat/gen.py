#!/usr/bin/env python3
"""
Generator soal (jangan diupload). XOR dengan repeating key pendek.
"""
FLAG = b"CTF{r3p34t1ng_x0r_k3y_1s_n0t_0t9}"
KEY = b"g0d"  # key pendek, 3 byte

def xor_repeat(data, key):
    return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

if __name__ == "__main__":
    ct = xor_repeat(FLAG, KEY)
    with open("output.txt", "w") as f:
        f.write(ct.hex() + "\n")
    print("hex:", ct.hex())
