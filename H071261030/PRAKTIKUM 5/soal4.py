def deteksi_anomali_email(email):
    error_list = []
    
    count_at = email.count("@")
    if count_at != 1:
        error_list.append("Harus memiliki tepat satu karakter @.")
        return error_list  
        
    local, domain = email.split("@")
    if local == "" or domain == "":
        error_list.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")

    if " " in email:
        error_list.append("Tidak boleh mengandung spasi di posisi manapun.")

    if local != "":
        if local.startswith(".") or local.endswith("."):
            error_list.append("Bagian local tidak boleh diawali atau diakhiri titik (.).")
        if ".." in local:
            error_list.append("Bagian local tidak boleh mengandung titik berurutan (..).")

    if domain != "":
        if "." not in domain:
            error_list.append("Bagian domain wajib memiliki minimal satu titik.")
        if ".." in domain or domain.endswith("."):
            error_list.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

    if not (email.endswith(".com") or email.endswith(".id") or email.endswith(".ac.id")):
        error_list.append("Wajib berakhiran dengan .com, .id, atau.ac.id")
        
    return error_list

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return

    max_len = 0
    for e in daftar_email_valid:
        if len(e) > max_len:
            max_len = len(e)
            
    lebar_kotak = max_len + 4  
    
    garis_border = "+" + (karakter_border * lebar_kotak) + "+"
    
    print(garis_border)
    print("| HASIL EMAIL VALID".ljust(lebar_kotak + 1) + "|")
    print(garis_border)
    for email in daftar_email_valid:
        isi = f"| {email} ".ljust(lebar_kotak + 1) + "|"
        print(isi)
    print(garis_border)

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_email_valid = []

while True:
    inp_email = input("Masukkan email: ").strip()
    
    if inp_email.lower() == "tutup":
        break
        
    if inp_email in daftar_email_valid:
        print(">> Email DITOLAK karena:")
        print("Email sudah terdaftar (Duplikat).")
        continue
        
    errors = deteksi_anomali_email(inp_email)
    
    if len(errors) == 0:
        print(">> Email VALID!")
        daftar_email_valid.append(inp_email)
    else:
        print(">> Email DITOLAK karena:")
        for err in errors:
            print(err)

cetak_daftar(daftar_email_valid, border)    