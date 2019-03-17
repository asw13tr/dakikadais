from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import *
from django import forms


# Kullanıcı seçme ekranı
class UyeChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # Yeni model
        model = Uye


#Yeni Kullanıcı oluşturma sınıfı
class UyeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Uye

    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            Uye.objects.get(username=username)
        except Uye.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['duplicate_username'])


class UyeAdmin(UserAdmin):
    form = UyeChangeForm
    list_display = ('is_active', 'username', 'full_name', 'email', 'telefon',)
    list_display_links = ['username']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': (
                    'telefon',          'cinsiyet',     'egitim',
                    'askerlik',         'uye_tipi',     'fotograf',
                    'dogum_tarihi',     'konum',        'hakkinda',
                    'website',          'facebook',     'twitter',
                    'google_plus',      'youtube',      'instagram',)}),
    )



admin.site.register(Uye, UyeAdmin)
