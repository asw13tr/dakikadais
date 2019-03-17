from django.db import models
from system.models import Sehir, Kategori
from main.functions import asw_unique_slug, get_slug
from django.contrib.auth import get_user_model
User = get_user_model()
from system.models import *
from datetime import datetime
from django.urls import reverse
from main.settings import TECRUBE_OPTIONS

##################
##### FİRMA MODELİ
class Firma(models.Model):
    slug            = models.SlugField(max_length=255,  verbose_name="Firma url adı", editable=False, null=True)
    adi             = models.CharField(max_length=255,  verbose_name='Firma Adı')
    telefon         = models.CharField(max_length=20,   verbose_name="Firma Telefon No",    blank=True, null=True, default="")
    yetkili         = models.CharField(max_length=255,  verbose_name="Firma Yetkilisi",     blank=True, null=True, default="")
    vergi_no        = models.CharField(max_length=255,  verbose_name="Vergi Numarası",      blank=True, null=True, default="")
    vergi_dairesi   = models.CharField(max_length=255,  verbose_name="Vergi Dairesi",       blank=True, null=True, default="")
    adres           = models.TextField(verbose_name="Firma Adresi", blank=True, null=True, default="")
    eposta          = models.EmailField(max_length=255, verbose_name="E-post adresi",   blank=True, null=True, default="")

    aciklama    = RichTextField(config_name='members', verbose_name='Firma Tanıtım Yazısı', blank=True, null=True, default="")

    kategori    = models.ForeignKey(Kategori, verbose_name="Kategori", on_delete=models.CASCADE, blank=True, null=True, default="")
    sehir       = models.ForeignKey(Sehir, verbose_name="Şehir", on_delete=models.CASCADE, blank=True, null=True, default="")

    uye         = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    durum       = models.BooleanField(verbose_name="Onaylanmış", default=False)

    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)

    def __str__(self):
        return self.adi


    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.adi)
        return super(Firma, self).save(*args, **kwargs)

    class Meta:
        db_table = "firmalar"
        verbose_name = "Firma"
        verbose_name_plural = "Firmalar"


##################
##### ILAN MODELİ
cinsiyet_secenekleri = ( ('F', 'Farketmez'), ('E', 'Erkek'), ('K', 'Kadın') )
class Ilan(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="İlan Başlığı")
    slug        = models.SlugField(max_length=255, verbose_name="İlan url adı", editable=False, null=True)
    firma       = models.ForeignKey(Firma, verbose_name="Çalışılacak Firma", on_delete=models.CASCADE)
    sehir       = models.ForeignKey(Sehir, verbose_name="Çalışılacak Şehir", on_delete=models.CASCADE)
    meslek      = models.ManyToManyField(Meslek, verbose_name="Meslek")
    tecrube     = models.PositiveSmallIntegerField(max_length=11, choices=TECRUBE_OPTIONS, default=0, verbose_name='Deneyim')
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
    detay	    = RichTextField(config_name='members', blank=True, verbose_name='İş Tanıtım Yazısı', default="")
    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)
    durum       = models.BooleanField(verbose_name="Yayımlanma", default=True)


    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Ilan, self).save(*args, **kwargs)

    def getKategoriStr(self):
        items = [ i[1] for i in list(self.kategori.values_list())]
        return " - ".join(items)

    def getMeslekStr(self):
        items = [ i[1] for i in list(self.meslek.values_list())]
        return " - ".join(items)

    def getMeslekUrls(self):
        pattern = '<a href="{}">{}</a>';
        items = [ pattern.format(i.get_absolute_url(), i.baslik) for i in list(self.meslek.all())]
        return " - ".join(items)


    def getZamanStr(self):
        items = [ i[1] for i in self.zaman.values_list() ]
        return " - ".join(items)

    def getMaasStr(self):
        return " - ".join( [ i[1]+" TL" for i in self.maas.values_list() ] )

    def getEgitimStr(self):
        items = [ i[1] for i in self.egitim.values_list() ]
        return " - ".join(items)

    def getAskerlikStr(self):
        items = [ i[1] for i in self.askerlik.values_list() ]
        return " - ".join(items)

    def getKonusulanDillerStr(self):
        items = [ i[1] for i in self.dil_konusma.values_list() ]
        return " - ".join(items)

    def getYazilanDillerStr(self):
        items = [ i[1] for i in self.dil_yazma.values_list() ]
        return " - ".join(items)

    def getTecrube(self):
        items = [v for k, v in TECRUBE_OPTIONS if k == self.tecrube]
        return "".join(items)

    def getCinsiyet(self):
        items = [v for k, v in cinsiyet_secenekleri if k == self.cinsiyet]
        return "".join(items)

    def get_absolute_url(self):
        sehir = get_slug( self.sehir.isim )
        return reverse('ilan_detay', kwargs={'slug':self.slug, 'id':self.id, 'sehir':sehir})

    def get_edit_url(self):
        return reverse('ilan_duzenle', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('ilan_sil', kwargs={'id':self.id})

    def get_filter_items_url(self):
        return reverse('uygun_istekler', kwargs={'id':self.id})

    class Meta:
        db_table = "ilanlar"
        verbose_name = "İş ilanı"
        verbose_name_plural = "İş ilanları"
        ordering = ['-id']



##################
##### Istek MODELİ
class Istek(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="İstek Başlığı")
    slug        = models.SlugField(max_length=255, verbose_name="İstek başlığı url adı", editable=False, null=True)
    uye         = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    sehir       = models.ForeignKey(Sehir, verbose_name="Çalışılacak Şehir", on_delete=models.CASCADE)
    meslek      = models.ForeignKey(Meslek, verbose_name="Meslek", on_delete=models.CASCADE)
    tecrube     = models.PositiveSmallIntegerField(max_length=11, choices=TECRUBE_OPTIONS, default=0, verbose_name='Deneyim')
    #kategori    = models.ManyToManyField(Kategori, verbose_name="İş Kategorisi")
    zaman       = models.ManyToManyField(Zaman, verbose_name="Zaman")
    maas        = models.ManyToManyField(Maas, verbose_name="İstenen Maaş")
    detay	    = RichTextField(config_name='members', blank=True, verbose_name='Detay', default="")
    c_time      = models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
    u_time      = models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)
    durum       = models.BooleanField(verbose_name="Yayımlanma", default=True)

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Istek, self).save(*args, **kwargs)

    def getKategoriStr(self):
        items = [ i[1] for i in list(self.kategori.values_list())]
        return " - ".join(items)

    def getZamanStr(self):
        items = [ i[1] for i in self.zaman.values_list() ]
        return " - ".join(items)

    def getMaasStr(self):
        items = [ i[1]+"₺" for i in self.maas.values_list() ]
        return " - ".join(items)

    def getTecrube(self):
        items = [v for k, v in TECRUBE_OPTIONS if k == self.tecrube]
        return "".join(items)

    def getMeslekStr(self):
        return self.meslek

    def getCinsiyet(self):
        items = [v for k, v in cinsiyet_secenekleri if k == self.uye.cinsiyet]
        return "".join(items)

    def getMeslekUrls(self):
        pattern = '<a href="{}">{}</a>';
        return pattern.format(self.meslek.get_istek_url(), self.meslek.baslik)

    def getKonusulanDillerStr(self):
        items = [ i[1] for i in self.uye.dil_konusma.values_list() ]
        return " - ".join(items)

    def getYazilanDillerStr(self):
        items = [ i[1] for i in self.uye.dil_yazma.values_list() ]
        return " - ".join(items)

    def get_absolute_url(self):
        sehir = get_slug( self.sehir.isim )
        return reverse('istek_detay', kwargs={'slug':self.slug, 'id':self.id})

    def get_edit_url(self):
        return reverse('istek_duzenle', kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('istek_sil', kwargs={'id':self.id})

    def get_filter_items_url(self):
        return reverse('uygun_ilanlar', kwargs={'id':self.id})

    class Meta:
        db_table = "istekler"
        verbose_name = "İş isteği"
        verbose_name_plural = "İş istekleri"
