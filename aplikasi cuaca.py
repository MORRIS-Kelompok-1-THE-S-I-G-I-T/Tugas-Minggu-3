"""
Aplikasi Informasi Cuaca
Dibuat sesuai flowchart: pilih daerah -> pilih menu informasi
-> tampilkan hasil -> ulangi menu / ganti daerah / selesai.

Struktur file (letakkan dalam satu folder):
    aplikasi_cuaca.py : program utama (alur flowchart)
    daerah.py         : data daerah + menu pilih daerah
    informasi.py      : ambil data cuaca BMKG, menu informasi, tips
    output.py         : tampilan judul dan hasil informasi
"""

from daerah import pilih_daerah
from informasi import ambil_cuaca, pilih_menu
from output import tampilkan_informasi, tampilkan_judul


def tanya_ya_tidak(pertanyaan):
    """Mengembalikan True jika jawaban 'ya', False jika 'tidak'."""
    while True:
        jawab = input(f"\n{pertanyaan} (y/t): ").strip().lower()
        if jawab in ("y", "ya"):
            return True
        if jawab in ("t", "tidak"):
            return False
        print("Jawab dengan 'y' atau 't'.")


def main():
    tampilkan_judul()

    ganti_daerah = True
    while ganti_daerah:
        daerah = pilih_daerah()
        cuaca = ambil_cuaca(daerah)

        menu_lain = True
        while menu_lain:
            menu = pilih_menu()
            tampilkan_informasi(cuaca, menu)
            menu_lain = tanya_ya_tidak("Ingin menu lain (dalam daerah yang sama)?")

        ganti_daerah = tanya_ya_tidak("Ingin pilih daerah lain?")

    print("\nTerima kasih telah menggunakan aplikasi. Selesai.")


if __name__ == "__main__":
    main()