from django import forms
from .models import *
from system.models import *
from django.forms.widgets import CheckboxSelectMultiple

class IsIstegiForm(forms.ModelForm):
    class Meta:
        model = Istek
        fields = ( 'baslik',  'sehir',  'meslek',  'tecrube',  'kategori', 'zaman',  'maas',  'detay')

    def __init__(self, *args, **kwargs):
        super(IsIstegiForm, self).__init__(*args, **kwargs)

        self.fields["kategori"].widget = CheckboxSelectMultiple()
        self.fields["kategori"].queryset = Kategori.objects.all()

        self.fields["zaman"].widget = CheckboxSelectMultiple()
        self.fields["zaman"].queryset = Zaman.objects.all()

        self.fields["maas"].widget = CheckboxSelectMultiple()
        self.fields["maas"].queryset = Maas.objects.all()

        #self.fields["meslek"].widget = CheckboxSelectMultiple()
        #self.fields["meslek"].queryset = Meslek.objects.all()


#########################################
class IlanForm(forms.ModelForm):
    class Meta:
        model = Ilan
        fields = ('baslik',  'sehir',  'meslek',  'tecrube',  'kategori',  'zaman',  'cinsiyet',  'yas_min',  'yas_max',  'maas',
                    'egitim',  'askerlik',  'dil_konusma',  'dil_yazma',  'detay' )

    def __init__(self, *args, **kwargs):
        super(IlanForm, self).__init__(*args, **kwargs)

        self.fields["kategori"].widget = CheckboxSelectMultiple()
        self.fields["kategori"].queryset = Kategori.objects.all()

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
