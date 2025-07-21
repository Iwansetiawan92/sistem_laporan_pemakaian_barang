from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    laporan = conn.execute('SELECT * FROM laporan').fetchall()
    conn.close()
    return render_template('index.html', laporan=laporan)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        tanggal = request.form['tanggal']
        departemen = request.form['departemen']
        nama_barang = request.form['nama_barang']
        jumlah = request.form['jumlah']
        satuan = request.form['satuan']

        conn = get_db_connection()
        conn.execute(
            'INSERT INTO laporan (tanggal, departemen, nama_barang, jumlah, satuan) VALUES (?, ?, ?, ?, ?)',
            (tanggal, departemen, nama_barang, jumlah, satuan)
        )
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('tambah.html')

if __name__ == '__main__':
    app.run(debug=True)

