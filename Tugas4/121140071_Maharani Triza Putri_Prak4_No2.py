import random

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.damage = 0
        self.jumlah_turn = 0

    def lakukan_aksi(self):
        pass

    def terima_aksi(self, damage):
        self.health -= damage

class Antares(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.health = 50000
        self.damage = 5000

    def lakukan_aksi(self):
        if self.jumlah_turn % 3 == 0:
            self.damage *= 1.5
            print(f"{self.name} meningkatkan serangannya menjadi {self.damage} DMG!")
        else:
            print(f"{self.name} menyerang sebanyak {self.damage} DMG!")
        self.jumlah_turn += 1

class Alphasetia(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.health = 40000
        self.damage = 6000

    def lakukan_aksi(self):
        if self.jumlah_turn % 2 == 0:
            self.health += 4000
            print(f"{self.name} menambah darah sebanyak 4000 HP!")
        else:
            print(f"{self.name} menyerang sebanyak {self.damage} DMG!")
        self.jumlah_turn += 1

class Lecalicus(Robot):
    def __init__(self, name):
        super().__init__(name)
        self.health = 45000
        self.damage = 5500

    def lakukan_aksi(self):
        if self.jumlah_turn % 4 == 0:
            self.health += 7000
            self.damage *= 2
            print(f"{self.name} meningkatkan serangannya menjadi {self.damage} DMG dan menambah darah sebanyak 7000 HP!")
        else:
            print(f"{self.name} menyerang sebanyak {self.damage} DMG!")
        self.jumlah_turn += 1

def main():
    print("Selamat datang di pertandingan robot Yamako")
    print("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus):")
    pilihan_robotmu = int(input())
    print("Pilih robot lawan (1 = Antares, 2 = Alphasetia, 3 = Lecalicus):")
    pilihan_lawan = int(input())

    if pilihan_robotmu == 1:
        robotmu = Antares("Antaresmu")
    elif pilihan_robotmu == 2:
        robotmu = Alphasetia("Alphasetiamu")
    elif pilihan_robotmu == 3:
        robotmu = Lecalicus("Lecalicusmu")
        
    if pilihan_lawan == 1:
        lawan = Antares("Antareslawan")
    elif pilihan_lawan == 2:
        lawan = Alphasetia("Alphasetialawan")
    elif pilihan_lawan == 3:
        lawan = Lecalicus("Lecalicuslawan")
        
    while robotmu.health > 0 and lawan.health > 0:
        robotmu.lakukan_aksi()
        lawan.terima_aksi(robotmu.damage)
        print(f"{robotmu.name} darah: {robotmu.health} HP")
        print(f"{lawan.name} darah: {lawan.health} HP\n")
        
    if robotmu.health > 0:
        print(f"Selamat, {robotmu.name} memenangkan pertandingan!")
    else:
        print(f"Sayang sekali, {robotmu.name} kalah dalam pertandingan.")
