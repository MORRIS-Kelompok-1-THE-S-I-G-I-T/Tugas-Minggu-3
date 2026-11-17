# KELOMPOK 1 : THE S.I.G.I.T

# DAFTAR ANGGOTA KELOMPOK
1. Alyssa Ivana Purnama (613260001) — Programmer
2. Arkan Muhammad Hujjatul Islam (714260010) — Programmer
3. Ataya Mahardika (714260013) — Penguji
4. Brilian Jovan Damanis (613260011) — Penulis Dokumentasi
5. Hafsoh Zahidah Nafisah (714260031) — Flowchart
6. Muhammad Sajid Algani (714260014) — Programmer
7. Radyth Tirta Prasetyo (614260023) — Video
8. Teuku Farel Febriansyah (714260028) — Poster

# APLIKASI INFORMASI CUACA

## 1. Deskripsi Aplikasi

Aplikasi Informasi Cuaca merupakan program berbasis Python yang digunakan untuk menampilkan informasi prakiraan cuaca dari BMKG (Badan Meteorologi, Klimatologi, dan Geofisika).

Aplikasi ini menyediakan informasi cuaca untuk tiga daerah, yaitu Kalimantan, Sulawesi, dan Jakarta. Pengguna dapat memilih daerah dan melihat informasi suhu, kondisi cuaca, kelembapan, kecepatan angin, tutupan awan, jarak pandang, serta tips pencegahan sesuai kondisi cuaca.

Program ini menggunakan API BMKG untuk mengambil data cuaca secara online. Jika data tidak dapat diakses, aplikasi akan menggunakan data contoh sebagai alternatif.

## 2. Fitur Aplikasi

1. **Pilih Daerah:** Menyediakan tiga pilihan daerah, yaitu Kalimantan, Sulawesi, dan Jakarta.
2. **Informasi Suhu dan Kondisi Cuaca:** Menampilkan suhu dalam derajat Celsius dan kondisi cuaca.
3. **Informasi Cuaca Lengkap:** Menampilkan kelembapan, kecepatan angin, arah angin, tutupan awan, dan jarak pandang.
4. **Tips Pencegahan:** Memberikan saran berdasarkan kondisi cuaca.
5. **Ulangi Menu:** Memungkinkan pengguna melihat informasi cuaca lainnya.
6. **Ganti Daerah:** Memungkinkan pengguna berpindah ke daerah lain.
7. **Validasi Input:** Memastikan pilihan pengguna sesuai dengan menu yang tersedia.
8. **Data Cadangan:** Menggunakan data contoh apabila API BMKG tidak dapat diakses.

## 3. Struktur File
```text
aplikasi-cuaca/
│
├── aplikasi_cuaca.py
├── daerah.py
├── informasi.py
├── output.py
└── README.md
```

### Keterangan File
- `aplikasi_cuaca.py`: File utama untuk menjalankan program.
- `daerah.py`: Mengatur data dan pilihan daerah.
- `informasi.py`: Mengambil data cuaca dari BMKG serta menyediakan informasi dan tips pencegahan.
- `output.py`: Mengatur tampilan judul dan hasil informasi cuaca.
- `README.md`: Berisi dokumentasi aplikasi.

## 4. Cara Penggunaan

### Persyaratan
- Python versi 3.6 atau lebih baru.
- Visual Studio Code atau terminal.
- Koneksi internet untuk mengambil data cuaca dari BMKG.
- Tidak memerlukan instalasi library tambahan.

### Langkah Menjalankan Program
1. Buka folder proyek melalui Visual Studio Code.
2. Pastikan seluruh file Python berada dalam satu folder.
3. Buka terminal pada Visual Studio Code.
4. Jalankan perintah berikut:

```bash
python aplikasi_cuaca.py
```

5. Pilih daerah yang ingin dilihat:
   - `1` untuk Kalimantan.
   - `2` untuk Sulawesi.
   - `3` untuk Jakarta.
6. Pilih jenis informasi cuaca yang ingin ditampilkan.
7. Ikuti pilihan menu untuk melihat informasi lainnya, mengganti daerah, atau keluar dari aplikasi.

**Catatan:** Jika koneksi internet atau API BMKG mengalami kendala, aplikasi akan menggunakan data contoh sebagai alternatif.