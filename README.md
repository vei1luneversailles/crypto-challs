# Crypto CTF Challenges (Static / No-NC)

Kumpulan soal CTF kategori Crypto yang **statis** — peserta cuma butuh file
yang disediakan, tidak perlu `nc` ke server manapun. Cocok untuk di-host
langsung di GitHub (misal untuk latihan internal, workshop, atau CTF
jamming kecil-kecilan).

## Daftar Soal

| # | Nama | Tingkat | Konsep |
|---|------|---------|--------|
| 01 | [Caesar++](01-caesar-plus/) | Easy | Rolling shift Caesar cipher |
| 02 | [XORientation](02-xor-repeat/) | Easy-Medium | Repeating-key XOR |
| 03 | [Small Gap RSA](03-small-rsa/) | Medium | RSA, Fermat factorization |
| 04 | [Predictable Seed](04-hash-lsb/) | Medium | Insecure PRNG (Python `random`) |

Setiap folder soal berisi:
- `README.md` — deskripsi soal + hint
- `chall.py` / `gen.py` — source (untuk soal yang menunjukkan source)
- `output.txt` — file yang harus diproses peserta untuk dapat flag

Folder `solutions/` berisi write-up penyelesaian (spoiler!) — jangan
disertakan kalau mau dipakai sebagai CTF sungguhan, atau taruh di branch
terpisah / private repo.

## Cara pakai untuk host sendiri

1. Ganti isi `FLAG` di masing-masing `gen.py`, lalu jalankan ulang untuk
   dapat `output.txt` baru.
2. Upload folder soal (tanpa `gen.py` dan tanpa folder `solutions/`) ke
   repo publik/GitHub Pages/GitHub Classroom, dsb.
3. Bagikan link repo ke peserta — semuanya offline, tidak perlu server
   apapun untuk soal-soal ini.

## Struktur

```
crypto-ctf/
├── README.md
├── 01-caesar-plus/
│   ├── README.md
│   ├── chall.py
│   ├── gen.py        
│   └── output.txt
├── 02-xor-repeat/
│   ├── README.md
│   ├── chall.py
│   ├── gen.py
│   └── output.txt
├── 03-small-rsa/
│   ├── README.md
│   ├── gen.py
│   └── output.txt
├── 04-hash-lsb/
│   ├── README.md
│   ├── gen.py
│   └── output.txt
└── solutions/        
    ├── solve_01_caesar_plus.py
    ├── solve_02_xor_repeat.py
    ├── solve_03_small_rsa.py
    └── solve_04_predictable_seed.py
```
