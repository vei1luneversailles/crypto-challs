#!/usr/bin/env python3
"""
Generator soal (jangan diupload). RSA dengan p,q berdekatan -> rentan Fermat factorization.
Butuh: pip install sympy
"""
from sympy import nextprime, isprime
import random

FLAG = b"CTF{f3rm47_f4ct0r1z4t10n_str1k3s_4g41n}"

def gen_close_primes(bits=512):
    base = random.getrandbits(bits)
    base |= (1 << (bits - 1)) | 1
    p = nextprime(base)
    q = nextprime(p + random.randint(1, 10_000))  # sangat dekat!
    return p, q

p, q = gen_close_primes()
n = p * q
e = 65537

m = int.from_bytes(FLAG, "big")
c = pow(m, e, n)

with open("output.txt", "w") as f:
    f.write(f"n = {n}\n")
    f.write(f"e = {e}\n")
    f.write(f"c = {c}\n")

print("n bit length:", n.bit_length())
print("done")
