class Insan:
    def __init__(self, ad, soyad, yas, ulke, sehir):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        self.ulke = ulke
        self.sehir = sehir
        self.yetenekler = []

    def kisi_bilgileri(self):
        return self.ad, self.soyad, self.yas, self.ulke, self.sehir, self.yetenekler

    def yetenek_ekle(self, yetenek):
        self.yetenekler.append(yetenek)


MFD = Insan("Muhammet Furkan", "DEMİRAL", "25", "Türkiye", "Kastamonu")
MFD.yetenek_ekle("Python")
MFD.yetenek_ekle("Bisiklete binmek")
print(MFD.kisi_bilgileri())