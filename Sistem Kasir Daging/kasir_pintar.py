"""
SISTEM KASIR PINTAR - TOKO DAGING
Program untuk mensimulasikan sistem kasir di toko daging dengan fitur diskon bersarang
"""

def tampilkan_header():
    """Menampilkan header program"""
    print("=" * 60)
    print("        SELAMAT DATANG DI SISTEM KASIR PINTAR TOKO DAGING")
    print("=" * 60)
    print()

def tampilkan_pricelist(harga_daging):
    """Menampilkan daftar harga daging"""
    print("DAFTAR HARGA DAGING:")
    print("-" * 40)
    for jenis, harga in harga_daging.items():
        print(f"  {jenis:<15} : Rp{harga:>10,}/kg")
    print("-" * 40)
    print()

def hitung_diskon(jenis, jumlah_kg, harga_satuan):
    """
    Menghitung diskon berdasarkan jenis daging dan jumlah kg
    Menggunakan nested if untuk logika diskon
    
    Args:
        jenis: jenis daging
        jumlah_kg: jumlah kg yang dibeli
        harga_satuan: harga per kg
    
    Returns:
        tuple: (subtotal, diskon)
    """
    subtotal = jumlah_kg * harga_satuan
    diskon = 0
    
    if jenis.lower() == "ayam":
        if jumlah_kg >= 5:
            diskon = subtotal * 0.10  # Diskon 10%
    elif jenis.lower() == "sapi":
        if jumlah_kg >= 2:
            diskon = subtotal * 0.15  # Diskon 15%
    elif jenis.lower() == "babi":
        if jumlah_kg >= 3:
            diskon = subtotal * 0.12  # Diskon 12%
    
    return subtotal, diskon

def format_rupiah(angka):
    """Mengformat angka menjadi format Rupiah"""
    return f"Rp{angka:,.0f}"

def main():
    # Data harga daging (Dictionary)
    harga_daging = {
        "Ayam": 15000,
        "Sapi": 12000,
        "Babi": 10000
    }
    
    tampilkan_header()
    tampilkan_pricelist(harga_daging)
    
    # List untuk menyimpan data pembelian
    riwayat_pembelian = []
    total_kotor = 0
    total_diskon = 0
    
    # While loop untuk input hingga user mengetik "cukup"
    while True:
        print("Masukkan jenis daging yang ingin dibeli")
        print("(atau ketik 'cukup' untuk selesai)")
        print()
        
        jenis = input("Jenis daging: ").strip()
        
        # Cek apakah user ingin berhenti
        if jenis.lower() == "cukup":
            break
        
        # Validasi jenis daging
        jenis_valid = False
        harga_satuan = 0
        jenis_benar = ""
        
        for daging in harga_daging.keys():
            if daging.lower() == jenis.lower():
                jenis_valid = True
                harga_satuan = harga_daging[daging]
                jenis_benar = daging
                break
        
        # Jika jenis daging tidak terdaftar
        if not jenis_valid:
            print("❌ PERINGATAN: Jenis daging tidak terdaftar!")
            print(f"   Pilih dari: {', '.join(harga_daging.keys())}")
            print()
            continue
        
        # Input jumlah kilogram
        try:
            jumlah_kg = float(input("Jumlah (kg): "))
            if jumlah_kg <= 0:
                print("❌ PERINGATAN: Jumlah harus lebih dari 0!")
                print()
                continue
        except ValueError:
            print("❌ PERINGATAN: Input harus berupa angka!")
            print()
            continue
        
        # Hitung subtotal dan diskon
        subtotal, diskon = hitung_diskon(jenis_benar, jumlah_kg, harga_satuan)
        total_bayar_item = subtotal - diskon
        
        # Simpan ke riwayat pembelian
        riwayat_pembelian.append({
            "jenis": jenis_benar,
            "kg": jumlah_kg,
            "harga_satuan": harga_satuan,
            "subtotal": subtotal,
            "diskon": diskon,
            "total": total_bayar_item
        })
        
        total_kotor += subtotal
        total_diskon += diskon
        
        # Tampilkan konfirmasi pembelian
        print()
        print("✓ Item ditambahkan ke keranjang:")
        print(f"  {jenis_benar} x {jumlah_kg} kg = {format_rupiah(subtotal)}")
        if diskon > 0:
            print(f"  Diskon: {format_rupiah(diskon)}")
            print(f"  Subtotal: {format_rupiah(total_bayar_item)}")
        print()
        print("-" * 60)
        print()
    
    # Jika tidak ada pembelian
    if len(riwayat_pembelian) == 0:
        print("\n⚠️  Tidak ada pembelian. Program berakhir.")
        return
    
    # Hitung total bersih
    total_bersih = total_kotor - total_diskon
    
    # Tampilkan detail keranjang
    print("\n" + "=" * 60)
    print("                    DETAIL PEMBELIAN")
    print("=" * 60)
    print()
    
    for i, item in enumerate(riwayat_pembelian, 1):
        print(f"{i}. {item['jenis']}")
        print(f"   Jumlah: {item['kg']} kg × {format_rupiah(item['harga_satuan'])}/kg")
        print(f"   Subtotal: {format_rupiah(item['subtotal'])}")
        if item['diskon'] > 0:
            persentase_diskon = (item['diskon'] / item['subtotal']) * 100
            print(f"   Diskon ({persentase_diskon:.0f}%): {format_rupiah(item['diskon'])}")
            print(f"   Total: {format_rupiah(item['total'])}")
        print()
    
    # Tampilkan nota pembayaran
    print("=" * 60)
    print("                    NOTA PEMBAYARAN")
    print("=" * 60)
    print()
    print(f"Total Kotor Belanjaan     : {format_rupiah(total_kotor)}")
    print(f"Total Potongan Diskon     : {format_rupiah(total_diskon)}")
    print("-" * 60)
    print(f"Total Bersih (Yang Dibayar): {format_rupiah(total_bersih)}")
    print()
    
    # Input uang pembayaran dari customer
    print("-" * 60)
    while True:
        try:
            uang_bayar = float(input("Uang pembayaran (Rp): "))
            if uang_bayar < total_bersih:
                print(f"❌ Uang tidak cukup! Kurang {format_rupiah(total_bersih - uang_bayar)}")
                continue
            break
        except ValueError:
            print("❌ Input harus berupa angka!")
    
    # Hitung kembalian
    kembalian = uang_bayar - total_bersih
    
    # Tampilkan struk akhir
    print()
    print("=" * 60)
    print("                        STRUK PEMBAYARAN")
    print("=" * 60)
    print()
    print(f"Total Belanjaan          : {format_rupiah(total_bersih)}")
    print(f"Uang Tunai Yang Dibayar  : {format_rupiah(uang_bayar)}")
    print(f"Kembalian                : {format_rupiah(kembalian)}")
    print()
    print("=" * 60)
    print("        TERIMA KASIH TELAH BERBELANJA DI TOKO KAMI!")
    print("=" * 60)
    print()

if __name__ == "__main__":
    main()
