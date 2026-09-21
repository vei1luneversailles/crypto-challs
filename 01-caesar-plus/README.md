# Caesar++ (Easy)

Kita tahu Caesar cipher itu gampang dibrute-force. Tapi kali ini shift-nya
bertambah 1 setiap huruf. Masih segampang itu?

**Files:** `chall.py`, `output.txt`

**Format flag:** `CTF{...}`

## Hint
- Karena flag diawali `CTF{`, kamu bisa hitung shift awal langsung dari
  4 karakter pertama ciphertext.
- Setelah shift awal ketemu, tinggal decode mundur sambil shift-nya
  dikurangi 1 tiap karakter.
