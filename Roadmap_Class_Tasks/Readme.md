# Insider Atlas Roadmap Class Tasks
[![-----------------------------------------------------](
https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png)](https://github.com/muhammetfurkandemiral?tab=repositories)

> ### Roadmap Class Task - 1
> 50 soruluk, 4 yanlışın 1 doğruyu götürdüğü sınavda öğrencinin inputlarla girilen doğru yanlış sayısına göre aldığı puanı hesaplayan programı yazınız.
> 
> - **Ogrenci sınıfı diye bir sınıf tanımlanacak.**
>  - Bu sınıfın içinde ogrenciAdı, ogrenciSoyadı, ogrenciSınıf’ı değişkenleri bulunacak. 
>  - Bu sınıftan nesne oluşturulurken bu bilgiler parametre olarak verilecek.
> - **Soru diye bir sınıfınız olacak.**
>  - Bu sınıfın NetSayısı(...) ve Hesapla(...) diye iki fonksiyon olacak.
>  - NetSayısı fonksiyonu doğru ve yanlış sayısını parametre olarak alıp öğrencinin kaç neti olduğunu bulur.
>  - Hesapla fonksiyonu net sayısını parametre olarak alıp öğrencinin puanını hesaplayacak. Her net 2 puan.
>  - En sonunda öğrenci bilgileri ve puanı console gösterilecek.
> 
> **Output**
> ![Roadmap_Class_1](https://user-images.githubusercontent.com/105215223/168570544-b586b0d1-6b1e-419a-bf4a-bf77f1650a0f.png)


 
> ### Roadmap Class Task - 2
> - **Insan isimli bir sınıf tanımlayınız.**
>  - Bütün constructor parametreleri default değerlere sahip olacak, default contructor (init) içinde belirlenecek. 
>  - Bu değerler; ad,soyad,yas,ulke,sehir olacak.
>  - Ek olarak yetenekler isimli bir boş dizi init fonksiyonu içinde tanımlanacak.
>  - kisi_bilgileri isimli fonksiyon ile init fonksiyonu içinde belirlenen kisi bilgileri return’le dönülecek.
>  - yetenek_ekle isimli fonksiyon ile init fonksiyonu içinde belirlenen yetenekler dizisine yetenekler eklenecek
> - Bu classtan belirtilen bilgileri içeren bir nesne tanımlayın.
>  - Tanımlanan nesneye yetenek ekleyin. (Bisiklete binmek, Python vs.)
>  - kisi_bilgileri fonksiyonu ile bu bilgileri gösterin.
> 
> **Output**
> ![Roadmap_Class_2](https://user-images.githubusercontent.com/105215223/168570793-eaa67e95-c511-484f-aae8-eb6adf5f7e0a.png)



> ### Roadmap Class Task - 3
> - **WebPush isimli bir class tanımlayınız.**
>  - WebPush class’ı send_push isimli bir fonksiyona sahip olsun
>  - Fonksiyon çağırıldığı zaman ‘Push gönderildi!’ yazısı gösterilsin. 
>  - Platform, optin, global_frequency_capping, start_date, end_date, language, push_type isimli özniteliklere sahip olsun. optin değeri boolean değer alsın.
> - **TriggerPush, BulkPush, SegmentPush, PriceAlertPush, InstockPush isimli classlar tanımlayınız.**
>  - Bu class’lar WebPush classından miras alsın.Miras alan classlar ana classtan farklı olarak aşağıdaki değişkenlere sahip olsun:
>  - https://user-images.githubusercontent.com/93590132/151860333-15f24a71-9793-41f2-b254-208954285429.png
>  - discountPrice(price_info, discount_rate) - Bu method üründe yapılan indirimi hesaplayacak ve return ile geri döndürecek.
>  - stockUpdate() - Bu method stock bilgisini güncelleyip return ile geri döndürecek. 
>    - Örneğin oluşturulan nesnenin stock bilgisi true ile false, false ise true yapacak.
> - Bütün push çeşitlerinden nesne oluşturup, methodlarını varsa kullanılmalı ve ana classta bulunan send_push methodu çağırılmalı.
> 
> **Output**
> ![Roadmap_Class_3](https://user-images.githubusercontent.com/105215223/168570866-4d5b830d-4090-4a8f-9464-c28001a92961.png)


