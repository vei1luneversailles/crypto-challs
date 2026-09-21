# XORientation (Easy-Medium)

Flag di-XOR pakai repeating key sepanjang 1-4 byte. Output ada di `output.txt`
(hex-encoded).

**Files:** `chall.py`, `output.txt`

**Format flag:** `CTF{...}`

## Hint
- Karena flag pasti diawali `CTF{`, kamu bisa XOR-kan ciphertext dengan
  plaintext yang diketahui untuk menebak potongan key, lalu cari
  periode (panjang key) yang bikin hasilnya konsisten/repeating.
