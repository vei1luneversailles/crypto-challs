#!/usr/bin/env python3
"""
Generator soal (jangan diupload). Flag dienkripsi pakai keystream dari
random.Random(seed) dengan seed = unix timestamp saat generate (diberi tahu
di soal, sengaja disempitkan rentangnya biar brute-force-able tanpa nc).
"""
import random, time

FLAG = b"CTF{pr3d1ct4bl3_s33d_pr4ng_bs_r4nd0m}"

# Untuk soal statis (no nc), kita "bekukan" waktu generate dan kasih tahu
# rentang pencarian di soal (misal +-500 detik dari waktu publish).
SEED = int(time.time())  # simulate: waktu saat challenge dibuat

def keystream(seed, length):
    rng = random.Random(seed)
    return bytes(rng.randrange(256) for _ in range(length))

ks = keystream(SEED, len(FLAG))
ct = bytes(a ^ b for a, b in zip(FLAG, ks))

published_hint = (SEED // 600) * 600  # dibulatkan ke kelipatan 600 detik (10 menit)

with open("output.txt", "w") as f:
    f.write(f"ciphertext_hex = {ct.hex()}\n")
    f.write(f"generated_near_unix_time = {published_hint}  # +- 600 detik\n")

print("SEED (rahasia sebenarnya, hanya utk verifikasi):", SEED)
