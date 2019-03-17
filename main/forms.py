from django import forms
from user.models import *
from ilan.models import Firma
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()

class UyeProfilFormu(UserCreationForm):
	class Meta:
		model = User
		fields = (  'tcno', 'first_name', 'last_name', 'email',  'telefon', 'cinsiyet', 'dogum_tarihi', 'egitim', 'askerlik', 'fotograf', 'sehir',
		 			'konum', 'hakkinda', 'website', 'facebook', 'twitter', 'google_plus', 'youtube', 'instagram' )

class HizliKayitFormu(UserCreationForm):
	class Meta:
		model = User
		fields = (  'username', 'password1', 'password2', 'email' )

class FirmaKayitFormu(forms.ModelForm):
	class Meta:
		model = Firma
		fields = (	'adi', 	 'telefon',  'eposta', 	 'yetkili',  'kategori',
					'sehir', 'adres', 	 'aciklama', 'vergi_no', 'vergi_dairesi' )

class UyeGirisFormu(forms.Form):
	username = forms.CharField(max_length=100, label='Kullanıcı Adı')
	password = forms.CharField(max_length=100, label='Şifresi', widget=forms.PasswordInput())
