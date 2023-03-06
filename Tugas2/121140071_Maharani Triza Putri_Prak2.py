class Mahasiswa:
    def __init__(self, nama, nim, kelas, jumlah_sks, semester, ipk):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.jumlah_sks = jumlah_sks
        self.semester = semester
        self.ipk = ipk

    def display_mahasiswa(self):
        print("Nama :", self.nama)
        print("NIM :", self.nim)
        print("Kelas :", self.kelas)
        print("Jumlah SKS :", self.jumlah_sks)
        print("Semester :", self.semester)
        print("IPK :", self.ipk)

mahasiswa1 = Mahasiswa("Maharani Triza Putri", "121140071", "RB", 22, 4, 3.35)
mahasiswa1.display_mahasiswa()