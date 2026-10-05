def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan = tujuan.upper()
    
    if asal not in ['C', 'F', 'K'] or tujuan not in ['C', 'F', 'K']:
        raise ValueError("Skala suhu tidak dikenali.")
    
    if asal == tujuan:
        return suhu
    
    if asal == "C":
        if tujuan == "F":
            return (suhu * 9 / 5) + 32
        elif tujuan == "K":
            return suhu + 273.15

    elif asal == "F":
        if tujuan == "C":
            return (suhu - 32) * 5 / 9
        elif tujuan == "K":
            return (suhu - 32) * 5 / 9 + 273.15

    elif asal == "K":
        if tujuan == "C":
            return suhu - 273.15
        elif tujuan == "F":
            return (suhu - 273.15) * 9 / 5 + 32
        

print("=== Konversi Suhu ===")

while True:
    nilai_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if nilai_suhu == "selesai":
        break
    
    try:    
        suhu = float(nilai_suhu)
    except ValueError as e:
        print(f"Error {e}")
        
    asal = input("Skala asal (C/F/K): ")
    tujuan = input("Skala tujuan (C/F/K): ")
    
    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print("Hasil:", suhu, asal.upper(), "=", hasil, tujuan.upper())
    except ValueError as pesan_error:
        print("Error:", pesan_error)
    # hasil = konversi_suhu(suhu, asal, tujuan)
    # print(f"hasil {suhu} {asal.upper()} = {hasil} {tujuan.upper()}")