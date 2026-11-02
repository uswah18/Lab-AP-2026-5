import re

def cek_username(username):
    pola = r"^[a-zA-Z]\w{4,11}$"
    return bool(re.match(pola, username))

def filter_username():
    print("=== Registrasi Username ===")
    print("Ketik 'SELESAI' untuk mengakhiri.")
    
    username_valid = []
    
    while True:
        username = input("Masukkan username: ")
        if username == "SELESAI":
            break
            
        if cek_username(username):
            print("Username tersedia.")
            username_valid.append(username)
        else:
            print("Username tidak valid!")
            
    print("\n=== Rekapitulasi ===")
    print("Username valid:")
    for i, user in enumerate(username_valid, 1):
        print(f"{i}. {user}")
    print(f"Jumlah username valid: {len(username_valid)}")
    
filter_username()