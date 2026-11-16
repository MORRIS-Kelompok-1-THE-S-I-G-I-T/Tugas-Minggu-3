"""
Modul informasi: pengambilan data cuaca (BMKG), menu informasi, dan tips.

Sumber data cuaca: BMKG via Data Prakiraan Cuaca Terbuka
(https://data.bmkg.go.id/prakiraan-cuaca/). Jika data BMKG tidak bisa
diambil (tanpa internet / API gangguan), dipakai data contoh.
"""

import json
import urllib.error
import urllib.request
from datetime import datetime, timezone

from daerah import DAERAH

SUMBER = "BMKG (Badan Meteorologi, Klimatologi, dan Geofisika)"
API_URL = "https://api.bmkg.go.id/publik/prakiraan-cuaca?adm4={kode}"

# Data contoh (cadangan jika BMKG tidak bisa diakses).
# Kunci sama dengan kunci di DAERAH.
DATA_CONTOH = {
    "1": {"suhu": 32, "kondisi": "Hujan Lebat", "kelembapan": 85,
            "angin": 10, "arah_angin": "Barat", "awan": 90, "jarak_pandang": "8"},
    "2": {"suhu": 30, "kondisi": "Berawan", "kelembapan": 75,
            "angin": 12, "arah_angin": "Timur", "awan": 60, "jarak_pandang": "10"},
    "3": {"suhu": 34, "kondisi": "Cerah Berawan", "kelembapan": 70,
            "angin": 8, "arah_angin": "Utara", "awan": 40, "jarak_pandang": "10"},
}


# ---------- Pengambilan data cuaca ----------

def pilih_slot_terdekat(cuaca_per_hari):
    """Pilih prakiraan (per 3 jam) yang waktunya paling dekat dengan sekarang."""
    semua = [slot for hari in cuaca_per_hari for slot in hari]
    sekarang = datetime.now(timezone.utc)

    def selisih(slot):
        try:
            waktu = datetime.strptime(slot["utc_datetime"], "%Y-%m-%d %H:%M:%S")
            return abs((waktu.replace(tzinfo=timezone.utc) - sekarang).total_seconds())
        except (KeyError, ValueError):
            return float("inf")

    return min(semua, key=selisih)


def ambil_cuaca_bmkg(kode_adm4):
    """Ambil cuaca dari BMKG. Mengembalikan dict, atau None jika gagal."""
    req = urllib.request.Request(
        API_URL.format(kode=kode_adm4),
        headers={"User-Agent": "aplikasi-cuaca-belajar/1.0"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.load(resp)
        lokasi = data["lokasi"]
        slot = pilih_slot_terdekat(data["data"][0]["cuaca"])
        return {
            "lokasi": f"{lokasi.get('desa', '-')}, {lokasi.get('kecamatan', '-')}, "
                        f"{lokasi.get('kotkab', '-')}, {lokasi.get('provinsi', '-')}",
            "suhu": slot.get("t"),
            "kondisi": slot.get("weather_desc", "-"),
            "kelembapan": slot.get("hu"),
            "angin": slot.get("ws"),
            "arah_angin": slot.get("wd", "-"),
            "awan": slot.get("tcc"),
            "jarak_pandang": slot.get("vs_text", "-"),
            "waktu": slot.get("local_datetime", "-"),
            "sumber": SUMBER,
        }
    except (urllib.error.URLError, TimeoutError, ValueError, KeyError, IndexError):
        return None


def ambil_cuaca(kode_daerah):
    """Ambil cuaca dari BMKG; jika gagal pakai data contoh."""
    daerah = DAERAH[kode_daerah]
    print(f"\nMengambil data cuaca {daerah['nama']} dari BMKG...")
    cuaca = ambil_cuaca_bmkg(daerah["adm4"])
    if cuaca is None:
        print("Gagal mengambil data BMKG, menampilkan data contoh.")
        cuaca = dict(DATA_CONTOH.get(kode_daerah, {}))
        cuaca["lokasi"] = daerah["nama"]
        cuaca["waktu"] = "-"
        cuaca["sumber"] = "Data contoh (bukan data aktual)"
    return cuaca


# ---------- Menu informasi ----------

def pilih_menu():
    """Menampilkan menu informasi dan mengembalikan pilihan yang valid."""
    while True:
        print("\nMenu Informasi:")
        print("1. Suhu dan Kondisi Cuaca")
        print("2. Informasi Cuaca")
        print("3. Pencegahan")
        pilihan = input("Masukkan pilihan (1-3): ").strip()
        if pilihan in ("1", "2", "3"):
            return pilihan
        print("Pilihan tidak valid, silakan coba lagi.")


def buat_tips(kondisi, suhu):
    """Tips pencegahan berdasarkan kondisi cuaca dan suhu."""
    k = str(kondisi).lower()
    tips = []
    if "hujan" in k:
        tips.append("Bawa payung atau jas hujan")
    if "petir" in k:
        tips.append("Hindari area terbuka dan pohon tinggi saat ada petir")
    if any(x in k for x in ("kabur", "kabut", "asap")):
        tips.append("Berkendara hati-hati, kurangi aktivitas luar ruangan, gunakan masker")
    if isinstance(suhu, (int, float)) and suhu >= 33:
        tips.append("Minum air yang cukup dan gunakan tabir surya")
    if not tips:
        tips.append("Cuaca relatif aman, tetap jaga kesehatan")
    return tips