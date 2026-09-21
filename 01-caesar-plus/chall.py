#!/usr/bin/env python3
"""
Caesar++
Shift bertambah 1 setiap karakter huruf (rolling shift).
Flag diketahui berawalan "CTF{" dan diakhiri "}".
"""

FLAG = open("flag.txt").read().strip()
START_SHIFT = ...  # dirahasiakan, integer 1-25

def encrypt(text, start_shift):
    out = []
    shift = start_shift
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            shift += 1
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    print(encrypt(FLAG, START_SHIFT))
