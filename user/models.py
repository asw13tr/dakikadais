from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField
from ckeditor.fields import RichTextField
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.urls import reverse
from system.models import Askerlik, Egitim, Sehir, Dil
from datetime import datetime


cinsiyet_secenekleri = ( ('B', 'Belirtilmemiş'), ('E', 'Erkek'), ('K', 'Kadın') )
uye_tipi_secenekleri = (
	('kullanici', 'Kullanıcı'),
	('is_veren', 'İş Veren')
)
class Uye(AbstractUser):
	tcno 			= models.CharField(max_length=11, verbose_name='TC Kimlik No', blank=True, null=True, default="")
	#eposta 			= models.EmailField(unique=True, verbose_name='E-posta Adresi', null=True, default=True)
	telefon			= models.CharField(max_length=20, verbose_name="Telefon Numarası", null=True, blank=True, default="")
	cinsiyet 		= models.CharField(max_length=1, choices=cinsiyet_secenekleri, blank=True, null=True, default='B', verbose_name='Cinsiyet')
	egitim			= models.ForeignKey(Egitim, blank=True, null=True, default=None, verbose_name="Egitim Durumu", on_delete=models.SET_NULL)
	askerlik		= models.ForeignKey(Askerlik, blank=True, null=True, default=None, verbose_name="Askerlik Durumu", on_delete=models.SET_NULL)
	uye_tipi		= models.CharField(max_length=15, choices=uye_tipi_secenekleri, blank=True, null=True, default='kullanici', verbose_name='Üyelik Durumu')
	fotograf		= StdImageField(upload_to='user-images', blank=True, variations={'thumbnail':(150, 150, True), 'medium':(300,300)}, verbose_name='Profil Fotoğrafı')
	dogum_tarihi 	= models.DateField(blank=True, null=True, verbose_name='Doğum Tarihi')
	sehir       	= models.ForeignKey(Sehir, verbose_name="Şehir", blank=True, null=True, default=None, on_delete=models.CASCADE)
	konum			= models.CharField(max_length=255, blank=True, verbose_name='Yaşadığınız Yer')
	hakkinda		= RichTextField(config_name='members', blank=True, verbose_name='Hakkınızda')
	website 		= models.URLField(max_length=200, blank=True, verbose_name='Website Adresi')
	facebook 		= models.URLField(max_length=255, blank=True, verbose_name='Facebook Profil Adresi')
	twitter 		= models.URLField(max_length=255, blank=True, verbose_name='Twitter Profil Adresi')
	google_plus 	= models.URLField(max_length=255, blank=True, verbose_name='Google+ Profil Adresi')
	youtube 		= models.URLField(max_length=255, blank=True, verbose_name='Youtube Profil Adresi')
	instagram 		= models.CharField(max_length=255, blank=True, verbose_name='İnstagram Kullanıcı Adı')
	goruntulenme	= models.IntegerField(default=0, editable=False, verbose_name='Görüntülenme')
	dil_konusma 	= models.ManyToManyField(Dil, verbose_name="Konuşabildiğiniz Diller", blank=True, null=True, default=None, related_name="konusulabilen_diller")
	dil_yazma   	= models.ManyToManyField(Dil, verbose_name="Yazıp, Okuyabildiğiniz Diller", blank=True, null=True, default=None, related_name="yazilabilen_diller")
	c_time      	= models.DateTimeField(verbose_name="Eklenme Tarihi", auto_now=True, editable=False, blank=True, null=True)
	u_time      	= models.DateTimeField(verbose_name="Güncellenme Tarihi", auto_now_add=True, editable=False, blank=True, null=True)

	def __str__(self):
		return self.username

	def get_yas(self):
		if not self.dogum_tarihi:
			return 0
		else:
			bugunTarihi = datetime.today()
			dogumTarihi = datetime( self.dogum_tarihi.year, self.dogum_tarihi.month, self.dogum_tarihi.day )
			yas =  int( (bugunTarihi - dogumTarihi).days / 365 )
			return yas




	def get_avatar(self):
		url = static('img/user-mask.jpg')
		if self.photo:
			url = self.photo.thumbnail.url
		else:
			if self.gender == 'E':
				url = static('img/user-man.png')
			elif self.gender == 'K':
				url = static('img/user-woman.png')
			else:
				url = static('img/user-mask.jpg')
		return url


	def full_name(self):
			return '{} {}'.format(self.first_name, self.last_name)


	def cinsiyeti(self):
		if self.gender == 'E':
			return 'Erkek'
		elif self.gender == 'K':
			return 'Kadın'
		else:
			return 'Belirtilmemiş'

	class Meta:
		db_table = 'uyeler'
		verbose_name = 'Kullanıcı'
		verbose_name_plural = 'Kullanıcılar'
