from django.shortcuts import render, HttpResponse
from .models import *
"""
doldur_egitim_durumlari = ('Yok', 'İlkokul', 'Ortaokul', 'Lise', 'Önlisans', 'Lisans', 'Yüksek Lisans', 'Doktora +')
doldur_askerlik_durumlari = ('Yapılmamış', 'Yapılmış', 'Tecilli', 'Muaf')
doldur_diller_kodlar  = ('en', 'de', 'ar', 'ru', 'fr', 'geo', 'es', 'zh', 'fa', 'ja')
doldur_diller_isimler = ('İngilizce', 'Almanca', 'Arapça', 'Rusça', 'Fransızca', 'Gürcüce', 'İspanyolca', 'Çince', 'Farsça', 'Japonca')
doldur_diller = tuple(zip( doldur_diller_kodlar, doldur_diller_isimler ))
doldur_maaslar = ('0-1600', '1600-2500', '2500-3500', '3500-5000', '5000 +')
doldur_zamanlar = ('Tam Zamanlı', 'Yarı Zamanlı', 'Serbest / Frelance', 'Stajyer')
doldur_sehirler = ((1, 'Adana'), (2, 'Adıyaman'), (3, 'Afyonkarahisar'), (4, 'Ağrı'), (5, 'Amasya'), (6, 'Ankara'), (7, 'Antalya'),
                (8, 'Artvin'), (9, 'Aydın'), (10, 'Balıkesir'), (11, 'Bilecik'), (12, 'Bingöl'), (13, 'Bitlis'), (14, 'Bolu'), (15, 'Burdur'),
                (16, 'Bursa'), (17, 'Çanakkale'), (18, 'Çankırı'), (19, 'Çorum'), (20, 'Denizli'), (21, 'Diyarbakır'), (22, 'Edirne'), (23, 'Elâzığ'),
                (24, 'Erzincan'), (25, 'Erzurum'), (26, 'Eskişehir'), (27, 'Gaziantep'), (28, 'Giresun'), (29, 'Gümüşhane'), (30, 'Hakkâri'), (31, 'Hatay'),
                (32, 'Isparta'), (33, 'Mersin'), (34, 'İstanbul'), (35, 'İzmir'), (36, 'Kars'), (37, 'Kastamonu'), (38, 'Kayseri'), (39, 'Kırklareli'),
                (40, 'Kırşehir'), (41, 'Kocaeli'), (42, 'Konya'), (43, 'Kütahya'), (44, 'Malatya'), (45, 'Manisa'), (46, 'Kahramanmaraş'), (47, 'Mardin'),
                (48, 'Muğla'), (49, 'Muş'), (50, 'Nevşehir'), (51, 'Niğde'), (52, 'Ordu'), (53, 'Rize'), (54, 'Sakarya'), (55, 'Samsun'),
                (56, 'Siirt'), (57, 'Sinop'), (58, 'Sivas'), (59, 'Tekirdağ'), (60, 'Tokat'), (61, 'Trabzon'), (62, 'Tunceli'), (63, 'Şanlıurfa'),
                (64, 'Uşak'), (65, 'Van'), (66, 'Yozgat'), (67, 'Zonguldak'), (68, 'Aksaray'), (69, 'Bayburt'), (70, 'Karaman'), (71, 'Kırıkkale'),
                (72, 'Batman'), (73, 'Şırnak'), (74, 'Bartın'), (75, 'Ardahan'), (76, 'Iğdır'), (77, 'Yalova'), (78, 'Karabük'), (79, 'Kilis'),
                (80, 'Osmaniye'), (81, 'Düzce'))
doldur_kategoriler = ('Bilgi Teknolojileri',  'Müşteri Hizmetleri / Çağrı Merkezi',  'Eğitim / Öğretim',  'Muhasebe / Finans / Mali İşler',  'Gayrimenkul / Emlak',  'Genel Başvuru',  'Güvenlik',
                    'Hizmet',  'Hukuk / Avukat',  'İdari İşler / Ofis',  'İnsan Kaynakları',  'İthalat / İhracat',  'Kafe / Bar / Restoran',  'Lojistik / Depo / Taşımacılık',
                    'Makine Operatörü',  'Market',  'Medya / Reklam / Tanıtım',  'Mühendislik',  'Operasyon',  'Pazarlama / Satış / Satın Alma',  'Proje / Yönetim ',  'Sağlık / Medikal',
                    'Mağaza / Perakende',  'Banka / Sigorta',  'Staj',  'Şoför',  'Tasarım / Grafik',  'Teknik İşler',  'Tekstil',  'Temizlik',
                    'Turizm - Otelcilik',  'Üretim / Kalite',  'Yapı / İnşaat / Mimarlık',  'Yazılım / Donanım / Bilgisayar',  'İş Sağlığı Ve Güvenliği',  'Otomotiv', 'Engelli' )
def veritabanini_doldur(request):
    for baslik in doldur_egitim_durumlari:
        Egitim.objects.get_or_create(baslik=baslik)
    for baslik in doldur_askerlik_durumlari:
        Askerlik.objects.get_or_create(baslik=baslik)
    for kod, baslik in doldur_diller:
        Dil.objects.get_or_create(baslik=baslik, kod=kod)
    for baslik in doldur_maaslar:
        Maas.objects.get_or_create(baslik=baslik)
    for baslik in doldur_zamanlar:
        Zaman.objects.get_or_create(baslik=baslik)
    for plaka, isim in doldur_sehirler:
        if plaka < 10: plaka = '0'+str(plaka)
        Sehir.objects.get_or_create(isim=isim, plaka=str(plaka))
    for baslik in doldur_kategoriler:
        Kategori.objects.get_or_create(baslik=baslik)

    return HttpResponse("Veritabanı Dolduruldu")
"""
