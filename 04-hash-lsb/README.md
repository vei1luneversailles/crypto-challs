# Predictable Seed (Medium)

Flag di-XOR dengan keystream dari `random.Random(seed)` Python. `seed` adalah
unix timestamp saat challenge ini dibuat — kita kasih tahu sekitar kapan.

**Files:** `output.txt`

**Format flag:** `CTF{...}`

## Hint
- `random` bawaan Python bukan CSPRNG. Kalau kamu tahu seed-nya (atau
  rentang kecil kemungkinan seed), kamu bisa regenerate keystream yang
  identik dan brute force sampai hasil XOR-nya membentuk teks yang masuk akal
  (diawali `CTF{`).
