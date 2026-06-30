import json
import os

def muat_data_menu():
    """Membaca file menu.json"""
    try:
        direktori_saat_ini = os.path.dirname(os.path.abspath(__file__))
        path_json = os.path.join(direktori_saat_ini, "menu.json")
        with open(path_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("❌ File menu.json tidak ditemukan!")
    except json.JSONDecodeError:
        print("❌ Format JSON tidak valid!")
    return None

def tampilkan_menu(data_menu):
    """Menampilkan daftar menu"""
    print("\n" + "=" * 50)
    print("           DAFTAR MENU RESTORAN")
    print("=" * 50)
    print("\n MAKANAN:")
    for item in data_menu["makanan"]:
        print(f"  {item['nama']:<25} Rp {item['harga']:>8,}")
    print("\n MINUMAN:")
    for item in data_menu["minuman"]:
        print(f"  {item['nama']:<25} Rp {item['harga']:>8,}")
    print("=" * 50)

def hitung_diskon(total_belanja, status_member):
    """Diskon sederhana: Member vs Reguler"""
    persentase = 0
    if status_member == "member":
        if total_belanja >= 50000:
            persentase = 10
        else:
            persentase = 5
    elif status_member == "reguler":
        if total_belanja >= 100000:
            persentase = 5
        else:
            persentase = 0
    diskon = total_belanja * (persentase / 100)
    return diskon, persentase

def format_rupiah(angka):
    return f"Rp{angka:,.0f}"

def jalankan_kasir():
    data_menu = muat_data_menu()
    if data_menu is None:
        return
    
    print("\n" + "=" * 50)
    print("     SELAMAT DATANG DI SISTEM KASIR RESTORAN")
    print("=" * 50)

    nama_pelanggan = input("\n📝 Nama pelanggan: ").strip()
    while True:
        status_member = input("   Status (member/reguler): ").strip().lower()
        if status_member in ["member", "reguler"]:
            break
        print("❌ Status tidak valid! Pilih: member atau reguler")

    tampilkan_menu(data_menu)

    pesanan = []
    total_kotor = 0

    while True:
        nama_item = input("\n🛒 Masukkan nama item (atau 'cukup' untuk selesai): ").strip()
        if nama_item.lower() == "cukup":
            break

        # Cari item di menu
        item = next((i for i in data_menu["makanan"] + data_menu["minuman"] if i["nama"].lower() == nama_item.lower()), None)
        if item is None:
            print("❌ Item tidak ditemukan!")
            continue

        try:
            jumlah = int(input(f"   Jumlah {item['nama']}: "))
            if jumlah <= 0:
                print("❌ Jumlah harus > 0!")
                continue
        except ValueError:
            print("❌ Input harus angka!")
            continue

        subtotal = item["harga"] * jumlah
        pesanan.append({"nama": item["nama"], "harga": item["harga"], "jumlah": jumlah, "subtotal": subtotal})
        total_kotor += subtotal
        print(f"   ✓ {item['nama']} x {jumlah} = {format_rupiah(subtotal)}")

    if not pesanan:
        print("\n⚠️ Tidak ada pesanan. Program berakhir.")
        return

    diskon, persen = hitung_diskon(total_kotor, status_member)
    total_bayar = total_kotor - diskon

    print("\n" + "=" * 50)
    print("               STRUK PEMBAYARAN")
    print("=" * 50)
    print(f"👤 Nama Pelanggan : {nama_pelanggan}")
    print(f"   Status         : {status_member.upper()}\n")
    print("📋 DETAIL PESANAN:")
    for i, item in enumerate(pesanan, 1):
        print(f"{i}. {item['nama']} - {item['jumlah']} x {format_rupiah(item['harga'])} = {format_rupiah(item['subtotal'])}")
    print("\nTotal Kotor : ", format_rupiah(total_kotor))
    print(f"Diskon ({persen}%) : -{format_rupiah(diskon)}")
    print("TOTAL BAYAR : ", format_rupiah(total_bayar))
    print("=" * 50)

    while True:
        try:
            bayar = float(input("\n💵 Uang pembayaran (Rp): "))
            if bayar < total_bayar:
                print(f"❌ Uang kurang {format_rupiah(total_bayar - bayar)}")
                continue
            break
        except ValueError:
            print("❌ Input harus angka!")

    print("\nKembalian : ", format_rupiah(bayar - total_bayar))
    print("=" * 50)
    print("🙏 TERIMA KASIH TELAH BERBELANJA 🙏")
    print("=" * 50)

if __name__ == "__main__":
    jalankan_kasir()
