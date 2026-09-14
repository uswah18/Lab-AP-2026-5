menu = ["Kopi Susu", "Matcha Latte", "Americano"]
harga = [18000, 22000, 15000]
jumlah = [4, 3, 5]

# Sub total masing masing menu
Sub_kopi = harga[0] * jumlah[0]
Sub_matcha = harga[1] * jumlah[1]
Sub_americano = harga[2] * jumlah[2]

# Sub total penjualan
Subtotal_pendapatan = [Sub_kopi, Sub_matcha, Sub_americano]

# Total seluruh pendapatan dan pendapatan bersih
Total_pendapatan = Sub_kopi + Sub_matcha + Sub_americano
BIAYA_OPERASIONAL = 15000
Pendapatan_bersih = Total_pendapatan - BIAYA_OPERASIONAL

# Menghitung total barang terjual dan kondisi target tercapai
Total_barang = jumlah[0] + jumlah[1] + jumlah[2]
Target_tercapai = (Total_pendapatan > 200000) and (Total_barang > 10)


print("- Laporan Penjualan Kopi Senja -")
print("Subtotal kopi susu:", Sub_kopi)
print("Subtotal matcha latte :", Sub_matcha)
print("Subtotal americano :", Sub_americano)
print("Total barang :", Total_barang)
print("Total pendapatan :", Total_pendapatan)
print("Pendapatan bersih :", Pendapatan_bersih)
print("Status target pencapai :", "Tercapai" if Target_tercapai else "Belum tercapai")
