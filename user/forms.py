from django import forms
#from captcha.fields import ReCaptchaField
from .models import *
from ilan.models import *
from system.models import *
from django.forms.widgets import CheckboxSelectMultiple


class UyeGirisFormu(forms.Form):
	username = forms.CharField(max_length=100, label='Kullanıcı Adı')
	password = forms.CharField(max_length=100, label='Şifresi', widget=forms.PasswordInput())
	#captcha = ReCaptchaField(label='Güvenlik Kontrolü')


from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()

######################################
class UyeKayitFormu(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'cinsiyet', 'password1', 'password2')

##########################################
class UyeGuncellemeFormu(forms.ModelForm):
	class Meta:
		model = User
		fields = (  'tcno', 'first_name', 'last_name', 'email',  'telefon', 'cinsiyet', 'dogum_tarihi', 'egitim', 'askerlik', 'fotograf', 'sehir',
		 			'konum', 'hakkinda', 'website', 'facebook', 'twitter', 'google_plus', 'youtube', 'instagram', 'dil_konusma', 'dil_yazma' )

	def __init__(self, *args, **kwargs):
		super(UyeGuncellemeFormu, self).__init__(*args, **kwargs)

		self.fields["dil_konusma"].widget = CheckboxSelectMultiple()
		self.fields["dil_konusma"].queryset = Dil.objects.all()

		self.fields["dil_yazma"].widget = CheckboxSelectMultiple()
		self.fields["dil_yazma"].queryset = Dil.objects.all()

##########################################
class FirmaGuncellemeFormu(forms.ModelForm):
	class Meta:
		model = Firma
		fields = ('adi', 'telefon',  'eposta',  'yetkili',  'kategori',  'sehir',  'adres',  'aciklama',  'vergi_no',  'vergi_dairesi')

####################################
class IsIstegiForm(forms.ModelForm):
    class Meta:
        model = Istek
        #fields = ( 'baslik',  'sehir',  'meslek',  'tecrube',  'kategori', 'zaman',  'maas',  'detay')
        fields = ( 'baslik',  'sehir',  'meslek',  'tecrube',  'zaman',  'maas',  'detay')

    def __init__(self, *args, **kwargs):
        super(IsIstegiForm, self).__init__(*args, **kwargs)

        #self.fields["kategori"].widget = CheckboxSelectMultiple()
        #self.fields["kategori"].queryset = Kategori.objects.all()

        self.fields["zaman"].widget = CheckboxSelectMultiple()
        self.fields["zaman"].queryset = Zaman.objects.all()

        self.fields["maas"].widget = CheckboxSelectMultiple()
        self.fields["maas"].queryset = Maas.objects.all()

#########################################
class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ('baslik',  'sehir',  'meslek',  'tecrube',    'zaman',  'cinsiyet',  'yas_min',  'yas_max',  'maas',
                    'egitim',  'askerlik',  'dil_konusma',  'dil_yazma',  'detay' )

    def __init__(self, *args, **kwargs):
        super(IlanForm, self).__init__(*args, **kwargs)

        #self.fields["kategori"].widget = CheckboxSelectMultiple()
        #self.fields["kategori"].queryset = Kategori.objects.all()

        self.fields["zaman"].widget = CheckboxSelectMultiple()
        self.fields["zaman"].queryset = Zaman.objects.all()

        self.fields["maas"].widget = CheckboxSelectMultiple()
        self.fields["maas"].queryset = Maas.objects.all()

        self.fields["meslek"].widget = CheckboxSelectMultiple()
        self.fields["meslek"].queryset = Meslek.objects.all()

        self.fields["egitim"].widget = CheckboxSelectMultiple()
        self.fields["egitim"].queryset = Egitim.objects.all()

        self.fields["askerlik"].widget = CheckboxSelectMultiple()
        self.fields["askerlik"].queryset = Askerlik.objects.all()

        self.fields["dil_konusma"].widget = CheckboxSelectMultiple()
        self.fields["dil_konusma"].queryset = Dil.objects.all()

        self.fields["dil_yazma"].widget = CheckboxSelectMultiple()
        self.fields["dil_yazma"].queryset = Dil.objects.all()
