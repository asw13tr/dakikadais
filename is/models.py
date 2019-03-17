from django.db import models
from system.models import Sehir, Kategori
from main.functions import asw_unique_slug
from django.contrib.auth import get_user_model
User = get_user_model()
from system.models import *
from datetime import datetime
"""
##################
##### FİRMA MODELİ
class Firma(models.Model):
    adi         = models.CharField(max_length=255, verbose_name='Firma Adı')
    slug        = models.SlugField(max_length=255, verbose_name="Firma url adı", editable=False, null=True)
    telefon     = models.CharField(max_length=20, verbose_name="Firma Telefon No")
    eposta      = models.EmailField(max_length=255, verbose_name="E-post adresi", null=True, default=None)
    yetkili     = models.CharField(max_length=255, verbose_name="Firma Yetkilisi")
    kategori    = models.ForeignKey(Kategori, verbose_name="Kategori", on_delete=models.CASCADE)
    sehir       = models.ForeignKey(Sehir, verbose_name="Şehir", on_delete=models.CASCADE)
    adres       = models.TextField(verbose_name="Firma Adresi", blank=True, default="")
    aciklama    = models.TextField(verbose_name="Firma Açıklaması")
    vergi_no    = models.CharField(max_length=255, verbose_name="Vergi Numarası")
    vergi_dairesi = models.CharField(max_length=255, verbose_name="Vergi Dairesi")
    uye         = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)
    durum       = models.BooleanField(verbose_name="Onaylanmış", default=False)

    def __str__(self):
        return self.adi

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.adi)
        return super(Firma, self).save(args, kwargs)

    class Meta:
        db_table = "firmalar"
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"


##################
##### ILAN MODELİ

cinsiyet_secenekleri = ( ('F', 'Farketmez'), ('E', 'Erkek'), ('K', 'Kadın') )
is_tecrubeleri = ( ('F', 'Farketmez'), ('az', '1 yıldan az'), ('1-3', '1-3 yıl'), ('3-5', '3-5 yıl'), ('5-10', '5-10 yıl'), ('deneyimli', '10 yıldan fazla') )
class Ilan(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="İlan Başlığı")
    slug        = models.SlugField(max_length=255, verbose_name="İlan url adı", editable=False, null=True)
    firma       = models.ForeignKey(Firma, verbose_name="Çalışılacak Firma", on_delete=models.CASCADE)
    sehir       = models.ForeignKey(Sehir, verbose_name="Çalışılacak Şehir", on_delete=models.CASCADE)
    meslek      = models.ManyToManyField(Meslek, verbose_name="Meslek")
    tecrube     = models.CharField(max_length=11, choices=is_tecrubeleri, default='F', verbose_name='Deneyim')
    kategori    = models.ManyToManyField(Kategori, verbose_name="İş Kategorisi")
    zaman       = models.ManyToManyField(Zaman, verbose_name="Çalışma Zamanı")
    cinsiyet    = models.CharField(max_length=1, choices=cinsiyet_secenekleri, default='F', verbose_name='Cinsiyet')
    yas_min     = models.SmallIntegerField(verbose_name="Minimum Yaş", default=18)
    yas_max     = models.SmallIntegerField(verbose_name="Maximum Yaş", default=45)
    maas        = models.ManyToManyField(Maas, verbose_name="Muhtemel Maaş")
    egitim      = models.ManyToManyField(Egitim, verbose_name="Eğitim Seviyesi")
    askerlik    = models.ManyToManyField(Askerlik, verbose_name="Askerlik Durumu")
    dil_konusma = models.ManyToManyField(Dil, verbose_name="Konuşulabilen Diller", blank=True, null=True, default=None, related_name="konusulan_diller")
    dil_yazma   = models.ManyToManyField(Dil, verbose_name="Yazılıp, Okunabilen Diller", blank=True, null=True, default=None, related_name="yazilan_diller")
    detay	= RichTextField(blank=True, verbose_name='İş Tanıtım Yazısı', default="")
    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)
    durum       = models.BooleanField(verbose_name="Yayımlanma", default=True)

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.adi)
        return super(Ilan, self).save(args, kwargs)

    class Meta:
        db_table = "ilanlar"
        verbose_name = "İş ilanı"
        verbose_name_plural = "İş ilanları"



##################
##### Istek MODELİ
is_tecrubeleri = ( ('F', 'Farketmez'), ('az', '1 yıldan az'), ('1-3', '1-3 yıl'), ('3-5', '3-5 yıl'), ('5-10', '5-10 yıl'), ('deneyimli', '10 yıldan fazla') )
class Istek(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="İstek Başlığı")
    slug        = models.SlugField(max_length=255, verbose_name="İstek başlığı url adı", editable=False, null=True)
    uye         = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    sehir       = models.ForeignKey(Sehir, verbose_name="Çalışılacak Şehir", on_delete=models.CASCADE)
    meslek      = models.ManyToManyField(Meslek, verbose_name="Meslek")
    tecrube     = models.CharField(max_length=11, choices=is_tecrubeleri, default='F', verbose_name='Deneyim')
    kategori    = models.ManyToManyField(Kategori, verbose_name="İş Kategorisi")
    zaman       = models.ManyToManyField(Zaman, verbose_name="İş Kategorisi")
    maas        = models.ManyToManyField(Maas, verbose_name="İstenen Maaş")
    detay	    = RichTextField(blank=True, verbose_name='Detay', default="")
    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)
    durum       = models.BooleanField(verbose_name="Yayımlanma", default=True)

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.adi)
        return super(Istek, self).save(args, kwargs)

    class Meta:
        db_table = "istekler"
        verbose_name = "İş isteği"
        verbose_name_plural = "İş istekleri"
"""
