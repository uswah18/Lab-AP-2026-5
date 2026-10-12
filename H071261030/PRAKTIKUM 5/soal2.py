def cek_kata(teks, kata):
    indeks_list = []
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    
    start = 0
    while True:
        idx = teks_lower.find(kata_lower, start)
        if idx == -1:
            break
        indeks_list.append(idx)
        start = idx + 1
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwqyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sebelum_kata = False
    if i == 0 or teks[i-1] not in alfabet:
        sebelum_kata = True
        
    setelah_kata = False
    idx_setelah = i + panjang
    if idx_setelah >= len(teks) or teks[idx_setelah] not in alfabet:
        setelah_kata = True
        
    return sebelum_kata and setelah_kata

def sensor_kata(teks, kata, simbol):
    semua_indeks = cek_kata(teks, kata)
    indeks_valid = []
    panjang_kata = len(kata)
    
    for idx in semua_indeks:
        if cek_batas_kata(teks, idx, panjang_kata):
            indeks_valid.append(idx)
            
    teks_hasil = ""
    last_idx = 0
    for idx in indeks_valid:
        teks_hasil += teks[last_idx:idx] + (simbol * panjang_kata)
        last_idx = idx + panjang_kata
    teks_hasil += teks[last_idx:]
    
    return teks_hasil, len(indeks_valid), indeks_valid

input_teks = input("Masukkan teks: ")
kata_target = input("Masukkan kata target: ")
simbol_sensor = input("Masukkan simbol: ")

hasil_teks, jumlah, list_indeks = sensor_kata(input_teks, kata_target, simbol_sensor)
print("Hasil teks:", hasil_teks)
print(f"Jumlah: {jumlah} Indeks: {list_indeks}")


