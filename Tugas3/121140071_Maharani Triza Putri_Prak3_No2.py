class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        AkunBank.list_pelanggan.append((no_pelanggan, nama_pelanggan))

    def lihat_menu(self):
        print("Selamat datang di Bank Jago")
        print(f"Halo {self.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo")
        print("2. Tarik tunai")
        print("3. Transfer saldo")
        print("4. Keluar")

    def lihat_saldo(self):
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")

    def tarik_tunai(self):
        jumlah_nominal = int(input("Masukkan jumlah nominal yang ingin ditarik: "))
        if jumlah_nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= jumlah_nominal
            print("Saldo berhasil ditarik!")

    def transfer(self):
        nominal = int(input("Masukkan nominal yang ingin ditransfer: "))
        no_rek = int(input("Masukkan no rekening tujuan: "))
        found = False
        for pelanggan in AkunBank.list_pelanggan:
            if no_rek == pelanggan[0]:
                found = True
                break
        if not found:
            print("No rekening tujuan tidak dikenal! Kembali ke menu utama.")
        elif nominal > self.__jumlah_saldo:
            print("Nominal saldo yang Anda punya tidak cukup!")
        else:
            self.__jumlah_saldo -= nominal
            print(f"Transfer Rp {nominal} ke {pelanggan[1]} sukses!")

# Membuat instansi AkunBank
Akun1 = AkunBank(1234, "Maharani", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)

# Memanggil fungsi-fungsi untuk simulasi
Akun1.lihat_menu()
nomor_input = int(input("Masukkan nomor input: "))
while nomor_input != 4:
    if nomor_input == 1:
        Akun1.lihat_saldo()
    elif nomor_input == 2:
        Akun1.tarik_tunai()
    elif nomor_input == 3:
        Akun1.transfer()
    else:
        print("Input tidak valid!")
    Akun1.lihat_menu()
    nomor_input = int(input("Masukkan nomor input: "))
print("Terima kasih telah menggunakan layanan Bank Jago.")
