tujuan_wisata = (input("Masukkan tujuan (pantai/pegunungan/kota)= ")).strip().lower()
waktu = (input("Masukkan waktu (pagi/malam)= ")).strip().lower()
tipe_pengunjung = (input("Masukkan tipe pengunjung (anak/dewasa)= ")).strip().lower()

match tujuan_wisata:
    case "pantai":
        if waktu == "pagi":
            print("Paket A")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "pegunungan":
        if waktu == "pagi" and tipe_pengunjung == "dewasa":
            print("Paket B")
        elif waktu == "malam" and tipe_pengunjung == "dewasa":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case "kota":
        if waktu == "malam":
            print("Paket C")
        else:
            print("Tidak ada paket yang cocok")
    case _:
        print("Tidak ada paket yang cocok")