def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    huruf_kecil = teks.lower()

    for karakter in huruf_kecil:
        if karakter in alfabet:
            teks_bersih += karakter

    return teks_bersih


def cek_palindrom(teks):
    teks_terbalik = teks[::-1]

    if teks == teks_terbalik:
        return True, -1

    for i in range(len(teks)):
        if teks[i] != teks_terbalik[i]:
            return False, i

    return True, -1


def inti_palindrom(teks):
    teks_bersih = bersihkan_teks(teks)
    n = len(teks_bersih)
    panjang = 0
    palindrom = ""
    indeks_awal = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_bersih[i:j]
            is_palin, _ = cek_palindrom(sub)

            if is_palin and len(sub) > panjang:
                panjang = len(sub)
                palindrom = sub
                indeks_awal = i

    return {
        "teks": palindrom,
        "panjang": panjang,
        "indeks_awal": indeks_awal
    }


teks = input("Masukkan teks: ")

print("Teks bersih:", bersihkan_teks(teks))
print(inti_palindrom(teks))