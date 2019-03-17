from django.db import models
from main.functions import asw_unique_slug, get_slug
from ckeditor.fields import RichTextField
from django.urls import reverse

###################
##### DİLLER MODELİ
class Sayfa(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="Sayfa Adı")
    slug        = models.SlugField(max_length=255, verbose_name="Url Yazısı", blank=True, default="")
    aciklama    = models.TextField(verbose_name="Açıklama", blank=True, default='')
    durum       = models.BooleanField(verbose_name="Sayfayı Yayımla", default=True)
    detay       = RichTextField(verbose_name="İçerik", default="")
    c_time      = models.DateTimeField(verbose_name="Oluşturulma", auto_now=True, editable=False)
    u_time      = models.DateTimeField(verbose_name="Güncellenme", auto_now_add=True, editable=False)
    views       = models.PositiveIntegerField(verbose_name="Görüntülenme", default=0)
    trash       = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return "%s"%(self.baslik)

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Sayfa, self).save(args, kwargs)

    class Meta:
        db_table = "sayfalar"
        verbose_name = "Sayfa"
        verbose_name_plural = "Sayfalar"

###################
##### DİLLER MODELİ
class Dil(models.Model):
    baslik = models.CharField(max_length=255, verbose_name="Dil Adı")
    kod    = models.CharField(max_length=4, verbose_name="Dil Kodu", null=True)
    slug   = models.SlugField(max_length=255, verbose_name="Dil Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Dil"
        verbose_name_plural = "Diller"
        db_table = 'diller'

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Dil, self).save(*args, **kwargs)

####################
##### MAAŞLAR MODELİ
class Maas(models.Model):
    baslik = models.CharField(max_length=255, verbose_name="Maaş Miktar Aralığı: Ör: 1500-3000")
    slug = models.SlugField(max_length=255, verbose_name="Maaş Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Maaş"
        verbose_name_plural = "Maaşlar"
        db_table = 'maaslar'

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Maas, self).save(*args, **kwargs)

######################
##### MESLEKLER MODELİ
class Meslek(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="Meslek Adı")
    aciklama    = models.TextField(verbose_name="Açıkalama", null=True, blank=True, default="")
    slug        = models.SlugField(max_length=255, verbose_name="Meslek Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Meslek"
        verbose_name_plural = "Meslekler"
        db_table = 'meslekler'

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('ilan_ara_meslek', kwargs={ 'meslek':self.slug, 'id':self.id })
        
    def get_istek_url(self):
        return reverse('istek_ara_meslek', kwargs={ 'meslek':self.slug, 'id':self.id })

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Meslek, self).save(*args, **kwargs)

######################
##### KATEGORİLER MODELİ
class Kategori(models.Model):
    baslik      = models.CharField(max_length=255, verbose_name="Meslek Adı")
    aciklama    = models.TextField(verbose_name="Açıkalama", null=True, blank=True, default="")
    slug        = models.SlugField(max_length=255, verbose_name="Meslek Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"
        db_table = 'kategoriler'

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Kategori, self).save(*args, **kwargs)

######################
##### ŞEHİRLER MODELİ
class Sehir(models.Model):
    plaka     = models.CharField(max_length=255, verbose_name="Plaka", null=True, blank=True, default="")
    isim      = models.CharField(max_length=255, verbose_name="Şehir Adı")

    class Meta:
        verbose_name = "Şehir"
        verbose_name_plural = "Şehirler"
        db_table = 'sehirler'
        ordering = ['plaka']

    def ilan_sayisi(self):
        return self.ilan_set.count()

    def istek_sayisi(self):
        return self.istek_set.count()

    def get_absolute_url(self):
        return reverse('ilan_ara_sehir', kwargs={ 'sehir':get_slug(self.isim), 'id':self.id })
    def get_istek_url(self):
        return reverse('istek_ara_sehir', kwargs={ 'sehir':get_slug(self.isim), 'id':self.id })

    def __str__(self):
        return self.isim


######################
##### EĞİTİM MODELİ
class Egitim(models.Model):
    baslik    = models.CharField(max_length=255, verbose_name="Eğitim Seviye Başlığı", null=True, blank=True, default="")
    slug      = models.SlugField(max_length=255, verbose_name="Eğitim Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitim Seviyeleri"
        db_table = 'egitim_seviyeleri'
        ordering = ['id']

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Egitim, self).save(*args, **kwargs)


######################
##### ASKERLİK MODELİ
class Askerlik(models.Model):
    baslik    = models.CharField(max_length=255, verbose_name="Askerlik Seçeneği", null=True, blank=True, default="")
    slug      = models.SlugField(max_length=255, verbose_name="Seçenek Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Askerlik Durumu"
        verbose_name_plural = "Askerlik Durumları"
        db_table = 'askerlik_durumlari'
        ordering = ['id']

    def __str__(self):
        return self.baslik

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Askerlik, self).save(*args, **kwargs)

######################
##### ZAMAN MODELİ
class Zaman(models.Model):
    baslik    = models.TextField(verbose_name="Askerlik Seçeneği", null=True, blank=True, default="")
    slug      = models.SlugField(max_length=255, verbose_name="Seçenek Url Adı", null=True, editable=False)

    class Meta:
        verbose_name = "Mesai Süresi"
        verbose_name_plural = "Mesai Süreleri"
        db_table = 'mesali_sureleri'
        ordering = ['id']

    def __str__(self):
        return self.baslik

    def get_absolute_url(self):
        return reverse('ilan_ara_zaman', kwargs={ 'zaman':get_slug(self.slug), 'id':self.id })

    def save(self, *args, **kwargs):
        self.slug = asw_unique_slug(self, self.baslik)
        return super(Zaman, self).save(*args, **kwargs)
