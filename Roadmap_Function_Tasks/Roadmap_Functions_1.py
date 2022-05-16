def bolunenSayiBulma(min_sayi, max_sayi, bolunecek_sayi):
    tam_bolunenler = []

    for sayi in range(min_sayi, max_sayi):
        if sayi % bolunecek_sayi == 0:
            tam_bolunenler.append(sayi)

    print("Tam bölünen sayılar: {}".format(tam_bolunenler))

    sayi_araligi = max_sayi - min_sayi
    toplam_sayi = len(tam_bolunenler)

    return "{} adet sayı tam bölünmüştür.".format(toplam_sayi), "Aralıkta {} adet sayı vardır.".format(sayi_araligi)


print(bolunenSayiBulma(2, 100, 5))