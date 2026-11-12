"""
Modul daerah: data daerah dan menu pilih daerah.

Untuk menambah/mengubah daerah, cukup edit DAERAH di file ini.
"""

# Kode wilayah (adm4 = kelurahan/desa) yang mewakili tiap daerah.
# Kode Jakarta (Gambir) berasal dari contoh resmi BMKG; kode Kalimantan &
# Sulawesi perlu Anda cek/sesuaikan.
DAERAH = {
    "1": {"nama": "Kalimantan", "adm4": "63.71.01.1001"},
    "2": {"nama": "Sulawesi", "adm4": "73.71.05.1001"},
    "3": {"nama": "Jakarta", "adm4": "31.71.01.1001"},
}


def pilih_daerah():
    """Menampilkan menu daerah dan mengembalikan pilihan yang valid."""
    while True:
        print("\nPilih Daerah:")
        for kode, d in DAERAH.items():
            print(f"{kode}. {d['nama']}")
        pilihan = input(f"Masukkan pilihan (1-{len(DAERAH)}): ").strip()
        if pilihan in DAERAH:
            return pilihan
        print("Pilihan tidak valid, silakan coba lagi.")