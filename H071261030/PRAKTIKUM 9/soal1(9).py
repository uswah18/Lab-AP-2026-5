class Pemain:
    def __init__(self, nama, id_pemain, role, nilai_kill, nilai_assist, nilai_objective):
        self.nama = nama
        self.id_pemain = id_pemain
        self.role = role
        self.nilai_kill = nilai_kill
        self.nilai_assist = nilai_assist
        self.nilai_objective = nilai_objective

    def hitung_skor_akhir(self):
        return (0.3 * self.nilai_kill) + (0.3 * self.nilai_assist) + (0.4 * self.nilai_objective)

    def status_peforma(self):
        skor = self.hitung_skor_akhir()
        if skor >= 60:
            return "Unggul"
        else:
            return "Perlu Evaluasi"

    def tampilkan_data(self):
        skor = self.hitung_skor_akhir()
        status = self.status_peforma()
        return f"{self.nama:<12} | {self.id_pemain:<10} | {self.role:<10} | {skor:<10.2f} | {status:<16} |"

data_pemain = []

while True:
    try:
        jumlah_pemain = int(input("\nMasukkan jumlah pemain: "))
        if jumlah_pemain <= 0:
            print("Jumlah pemain harus lebih dari 0!")
            continue
        break
    except ValueError:
        print("Input yang Anda masukkan tidak valid! Harap masukkan angka.")

pemain = 1
while pemain <= jumlah_pemain:
    print(f"\n-- Data Pemain ke-{pemain} --")
    data_nama = input(f"{'Nama':<15}: ")
    data_id = input(f"{'ID Pemain':<15}: ")
    data_role = input(f"{'Role':<15}: ")
    
    while True:
        try:
            data_kill = int(input(f"{'Nilai Kill':<15}: "))
            if data_kill < 0:
                print("Nilai Kill tidak boleh negatif! Masukkan angka positif.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            
    while True:
        try:
            data_assist = int(input(f"{'Nilai Assist':<15}: "))
            if data_assist < 0:
                print("Nilai Assist tidak boleh negatif! Masukkan angka positif.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
            
    while True:
        try:
            data_objective = int(input(f"{'Nilai Objective':<15}: "))
            if data_objective < 0:
                print("Nilai Objective tidak boleh negatif! Masukkan angka positif.")
                continue
            break
        except ValueError:
            print("Input tidak valid! Harap masukkan angka.")
    
    isi_data_pemain = Pemain(data_nama, data_id, data_role, data_kill, data_assist, data_objective)
    data_pemain.append(isi_data_pemain)
    pemain += 1

print("\n--- REKAPITULASI PERFORMA PEMAIN ---")
print("=" * 78)
print(f"| {'No':<3} | {'Nama':<12} | {'ID Pemain':<10} | {'Role':<10} | {'Skor Akhir':<10} | {'Status':<16} |")
print("=" * 78)

for i, isi in enumerate(data_pemain, start=1):
    print(f"| {i:<3} | " + isi.tampilkan_data())

print("=" * 78)