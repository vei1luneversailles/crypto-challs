#!/usr/bin/env python3
"""
Generator soal (JANGAN diupload ke repo publik, cukup output-nya saja).
Caesar++ : shift bertambah 1 tiap karakter (rolling shift), mulai dari key awal.
"""
import random

FLAG = "CTF{r0ll1ng_c43s4r_1s_st1ll_c43s4r_af7er_all}"
START_SHIFT = random.randint(1, 25)

def encrypt(text, start_shift):
    out = []
    shift = start_shift
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            shift += 1  # shift bertambah tiap huruf
        else:
            out.append(ch)
    return "".join(out)

if __name__ == "__main__":
    ct = encrypt(FLAG, START_SHIFT)
    with open("output.txt", "w") as f:
        f.write(ct + "\n")
    print("Ciphertext:", ct)
    print("(start shift dirahasiakan, jangan commit ini)")
