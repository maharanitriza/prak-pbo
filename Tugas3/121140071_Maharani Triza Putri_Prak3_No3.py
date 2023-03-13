class Mobil:
    jumlah_mobil = 0
    
    def __init__(self, merek, tahun, harga, jumlah_roda):
        self.merek = merek
        self.tahun = tahun
        self.harga = harga
        self.jumlah_roda = jumlah_roda
        Mobil.jumlah_mobil += 1
    
    def get_harga(self):
        return self._harga
    
    def set_harga(self, harga_baru):
        self._harga = harga_baru
    
    def get_merek(self):
        return self._merek
    
    def get_jumlah_roda(self):
        return self.__jumlah_roda
