def notGiris():
    vize1 = int(input("Vize1:"))
    vize2 = int(input("Vize2:"))
    final = int(input("Final:"))

    if 0 < vize1 < 101 and 0 < vize2 < 101 and 0 < final < 101:
        not_ortalama = (float(vize1) * 0.3) + (float(vize2) * 0.3) + (float(final) * 0.4)
        harfNotuHesapla(not_ortalama)
    else:
        print("Lütfen 0-100 arasında bir not giriniz!")
        notGiris()


def harfNotuHesapla(ortalama):
    if ortalama >= 90:
        print(ortalama, "-----> AA")
    elif ortalama >= 85:
        print(ortalama, "-----> BA")
    elif ortalama >= 80:
        print(ortalama, "-----> BB")
    elif ortalama >= 75:
        print(ortalama, "-----> CB")
    elif ortalama >= 70:
        print(ortalama, "-----> CC")
    elif ortalama >= 65:
        print(ortalama, "-----> DC")
    elif ortalama >= 60:
        print(ortalama, "-----> DD")
    elif ortalama >= 55:
        print(ortalama, "-----> FD")
    else:
        print(ortalama, "-----> FF")


notGiris()