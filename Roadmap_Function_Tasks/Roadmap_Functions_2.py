def sayiOkunusu(sayi):
    birler = {1: "bir", 2: "iki", 3: "üç", 4: "dört", 5: "beş",
              6: "altı", 7: "yedi", 8: "sekiz", 9: "dokuz"}

    onlar = {10: "On", 20: "Yirmi", 30: "Otuz", 40: "Kırk", 50: "Elli",
             60: "Altmış", 70: "Yetmiş", 80: "Seksen", 90: "Doksan"}

    birler_basamagi = sayi % 10
    onlar_basamagi = sayi - birler_basamagi

    if birler_basamagi == 0:
        print(onlar[onlar_basamagi])
    else:
        print(onlar[onlar_basamagi], birler[birler_basamagi])


def sayiAtama():
    sayi = int(input("İki basamaklı bir sayı giriniz:"))

    if 9 < sayi < 100:
        sayiOkunusu(sayi)
    else:
        print("Geçersiz sayı girdiniz!")
        sayiAtama()


sayiAtama()