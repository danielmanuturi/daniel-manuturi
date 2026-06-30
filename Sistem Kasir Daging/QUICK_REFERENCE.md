# 📌 QUICK REFERENCE - SISTEM KASIR PINTAR

## 🎯 Struktur Program

```
┌─────────────────────────────────────────┐
│  HEADER & PRICELIST DISPLAY             │
├─────────────────────────────────────────┤
│  WHILE LOOP - INPUT PEMBELIAN           │
│  ├─ Input jenis daging                  │
│  ├─ Validasi jenis                      │
│  ├─ Input jumlah kg                     │
│  ├─ Validasi jumlah                     │
│  ├─ NESTED IF - HITUNG DISKON           │
│  ├─ Simpan ke riwayat                   │
│  └─ Tampilkan konfirmasi                │
├─────────────────────────────────────────┤
│  DETAIL PEMBELIAN                       │
├─────────────────────────────────────────┤
│  NOTA PEMBAYARAN                        │
│  ├─ Total Kotor                         │
│  ├─ Total Diskon                        │
│  └─ Total Bersih                        │
├─────────────────────────────────────────┤
│  INPUT UANG & HITUNG KEMBALIAN          │
├─────────────────────────────────────────┤
│  STRUK PEMBAYARAN AKHIR                 │
└─────────────────────────────────────────┘
```

## 💾 Data Structure

### Pricelist (Dictionary)
```python
{
    "Ayam": 15000,
    "Sapi": 12000,
    "Babi": 10000
}
```

### Item Pembelian (Dictionary dalam List)
```python
{
    "jenis": "Ayam",
    "kg": 6.0,
    "harga_satuan": 15000,
    "subtotal": 90000,
    "diskon": 9000,
    "total": 81000
}
```

## 🏷️ Harga & Diskon

| Jenis  | Harga/kg | Min. kg | Diskon |
|--------|----------|---------|--------|
| Ayam   | 15.000   | 5       | 10%    |
| Sapi   | 12.000   | 2       | 15%    |
| Babi   | 10.000   | 3       | 12%    |

## 🔄 Alur Perulangan (While Loop)

```
WHILE TRUE:
├─ Input jenis daging
├─ IF jenis == "cukup"
│  └─ BREAK
├─ Validasi jenis
│  ├─ IF tidak valid
│  │  └─ CONTINUE (minta input ulang)
│  └─ ELSE lanjut
├─ Input jumlah kg
│  ├─ TRY-EXCEPT untuk validasi
│  ├─ IF kg <= 0
│  │  └─ CONTINUE (minta input ulang)
│  └─ ELSE lanjut
├─ Hitung diskon (NESTED IF)
├─ Simpan ke riwayat
├─ Update total
└─ Tampilkan konfirmasi
```

## 📊 Nested IF untuk Diskon

```python
if jenis.lower() == "ayam":           # Level 1: IF
    if jumlah_kg >= 5:                # Level 2: IF (NESTED)
        diskon = subtotal * 0.10

elif jenis.lower() == "sapi":         # Level 1: ELIF
    if jumlah_kg >= 2:                # Level 2: IF (NESTED)
        diskon = subtotal * 0.15

elif jenis.lower() == "babi":         # Level 1: ELIF
    if jumlah_kg >= 3:                # Level 2: IF (NESTED)
        diskon = subtotal * 0.12
```

**Struktur Nested**: 2 level kondisional
- Level 1: Cek jenis daging
- Level 2: Cek jumlah minimum

## 🧮 Perhitungan Rumus

### Subtotal
```
Subtotal = Jumlah kg × Harga per kg
```

### Diskon
```
Diskon = Subtotal × Persentase Diskon
```

### Total Item
```
Total Item = Subtotal - Diskon
```

### Total Kotor (Semua Item)
```
Total Kotor = Σ (Semua Subtotal)
```

### Total Diskon (Semua Item)
```
Total Diskon = Σ (Semua Diskon)
```

### Total Bersih
```
Total Bersih = Total Kotor - Total Diskon
```

### Kembalian
```
Kembalian = Uang Pembayaran - Total Bersih
```

## ✅ Validasi Input

### Jenis Daging
- ✓ Ayam, Sapi, Babi (case-insensitive)
- ✓ String "cukup" untuk berhenti
- ✗ Jenis lain → Error message

### Jumlah Kilogram
- ✓ Angka positif (>0)
- ✓ Desimal (1.5, 2.7, dll)
- ✗ Angka <= 0 → Error message
- ✗ Text/non-numeric → Error message

### Uang Pembayaran
- ✓ Angka >= Total Bersih
- ✗ Angka < Total Bersih → Minta ulang
- ✗ Text/non-numeric → Error message

## 🎨 Output Format

### Pricelist Display
```
DAFTAR HARGA DAGING:
----------------------------------------
  Ayam            : Rp    15,000/kg
  Sapi            : Rp    12,000/kg
  Babi            : Rp    10,000/kg
----------------------------------------
```

### Item Confirmation
```
✓ Item ditambahkan ke keranjang:
  Ayam x 6.0 kg = Rp90,000
  Diskon: Rp9,000
  Subtotal: Rp81,000
```

### Nota Pembayaran
```
============================================================
                    NOTA PEMBAYARAN
============================================================

Total Kotor Belanjaan     : Rp146,000
Total Potongan Diskon     : Rp14,400
------------------------------------------------------------
Total Bersih (Yang Dibayar): Rp131,600
```

### Struk Akhir
```
============================================================
                        STRUK PEMBAYARAN
============================================================

Total Belanjaan          : Rp131,600
Uang Tunai Yang Dibayar  : Rp150,000
Kembalian                : Rp18,400
```

## 🚀 Cara Menjalankan

```bash
# 1. Buka terminal
cd "c:\Users\LENOVO\Documents\Belajar Python\Sistem_Kasir_Pintar"

# 2. Jalankan program
python kasir_pintar.py

# 3. Ikuti petunjuk
# - Input jenis daging
# - Input jumlah kg
# - Ulangi hingga selesai
# - Ketik "cukup" untuk selesai
```

## 📋 List Fungsi

| Fungsi | Parameter | Return | Kegunaan |
|--------|-----------|--------|----------|
| `tampilkan_header()` | - | - | Tampilkan judul program |
| `tampilkan_pricelist()` | dict | - | Tampilkan daftar harga |
| `hitung_diskon()` | str, float, float | tuple | Hitung diskon (nested if) |
| `format_rupiah()` | float | str | Format angka jadi rupiah |
| `main()` | - | - | Fungsi utama program |

## 🐛 Troubleshooting

| Masalah | Penyebab | Solusi |
|---------|----------|--------|
| Program tidak start | File tidak ada | Cek path folder |
| Input desimal error | Pakai koma (,) | Gunakan titik (.) |
| Validasi tidak bekerja | Typo di validasi | Cek syntax |
| Diskon tidak dihitung | Kondisi nested if salah | Cek logika diskon |
| Tampilan berantakan | Encoding terminal | Ganti ke UTF-8 |

## 📚 Konsep Python yang Digunakan

- ✓ **Dictionary**: Pricelist data
- ✓ **List**: Riwayat pembelian
- ✓ **While Loop**: Input berkelanjutan
- ✓ **IF-ELIF-ELSE**: Validasi & logika
- ✓ **Nested IF**: Hitung diskon
- ✓ **Function**: Modular code
- ✓ **String Methods**: `.lower()`, `.strip()`
- ✓ **Try-Except**: Error handling
- ✓ **For Loop**: Iterasi riwayat
- ✓ **Tuple**: Return multiple values
- ✓ **F-strings**: String formatting

## 🎓 Level Kesulitan

- **Beginner**: Memahami alur program, input-output
- **Intermediate**: Nested IF, validasi, error handling
- **Advanced**: Refactoring, optimization, extension

---

**Last Updated**: 2026-06-30  
**Version**: 1.0  
**Status**: ✓ Complete
