"""
Modul output: semua tampilan ke layar (judul dan hasil informasi).
"""

from informasi import SUMBER, buat_tips


def tampilkan_judul():
    print("=" * 44)
    print("       APLIKASI INFORMASI CUACA")
    print(f"  Sumber data: {SUMBER}")
    print("=" * 44)


def tampilkan_informasi(cuaca, menu):
    print(f"\n--- {cuaca['lokasi']} ---")
    if cuaca.get("waktu", "-") != "-":
        print(f"Prakiraan waktu setempat: {cuaca['waktu']}")
    if menu == "1":
        print(f"Suhu dan Kondisi Cuaca: {cuaca['suhu']}°C, {cuaca['kondisi']}")
    elif menu == "2":
        print("Informasi Cuaca:")
        print(f"  Kelembapan   : {cuaca['kelembapan']}%")
        print(f"  Angin        : {cuaca['angin']} km/jam dari {cuaca['arah_angin']}")
        print(f"  Tutupan awan : {cuaca['awan']}%")
        print(f"  Jarak pandang: {cuaca['jarak_pandang']} km")
    else:
        print("Tips Pencegahan:")
        for tip in buat_tips(cuaca["kondisi"], cuaca["suhu"]):
            print(f"  - {tip}")
    print(f"Sumber: {cuaca['sumber']}")