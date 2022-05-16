class Ogrenci():
    def __init__(self, ogrenci_adi, ogrenci_soyadi, ogrenci_sinif):
        self.ogrenciAdi = ogrenci_adi
        self.ogrenciSoyadi = ogrenci_soyadi
        self.ogrenciSinif = ogrenci_sinif


class Soru(Ogrenci):
    def net_sayisi(self):
        dogru_sayisi = float(input("Doğru soru sayısı = "))
        yanlis_sayisi = float(input("Yanlış soru sayısı = "))

        if dogru_sayisi + yanlis_sayisi != 50:
            print("Soru sayısı toplamı 50 olmalı")
            return self.net_sayisi()

        net = dogru_sayisi - (yanlis_sayisi * 0.25)
        self.hesapla(net)

    def hesapla(self, net=0.0):
        puan = net * 2
        print("{}. sınıf öğrencisi {} {}'ın neti = {}, puanı ise = {}".format
              (self.ogrenciSinif, self.ogrenciAdi, self.ogrenciSoyadi, net, puan))


MFD = Ogrenci("Muhammet Furkan", "DEMİRAL", "1")
Soru(MFD.ogrenciAdi, MFD.ogrenciSoyadi, MFD.ogrenciSinif).net_sayisi()