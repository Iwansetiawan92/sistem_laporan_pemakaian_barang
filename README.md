# Aplikasi Laporan Pemakaian Barang

Aplikasi web sederhana menggunakan Flask dan SQLite untuk mencatat laporan pemakaian barang.

## Fitur:
- Melihat laporan
- Menambahkan laporan baru

## Cara Menjalankan

1. Clone repo:

2. Install dependencies:

3. Buat database:

```python
import sqlite3
conn = sqlite3.connect('database.db')
conn.execute('''
    CREATE TABLE laporan (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tanggal TEXT NOT NULL,
        departemen TEXT NOT NULL,
        nama_barang TEXT NOT NULL,
        jumlah INTEGER NOT NULL,
        satuan TEXT NOT NULL
    )
''')
conn.close()
