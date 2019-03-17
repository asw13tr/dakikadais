from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', duzenle, name='hesap'),
    path('duzenle', duzenle, name='hesap_duzenle'),
    path('firma', duzenle_firma, name='firma_duzenle'),
    path('sifre', sifre_degistir, name='sifre_degistir'),

    path('isteklerim', isteklerim, name='isteklerim'),
    path('istek-olustur', istek_olustur, name='istek_olustur'),
    path('istek-duzenle/<int:id>', istek_duzenle, name='istek_duzenle'),
    path('istek-sil/<int:id>', istek_sil, name='istek_sil'),

    path('ilanlarim', ilanlarim, name='ilanlarim'),
    path('ilan-olustur', ilan_olustur, name='ilan_olustur'),
    path('ilan-duzenle/<int:id>', ilan_duzenle, name='ilan_duzenle'),
    path('ilan-sil/<int:id>', ilan_sil, name='ilan_sil'),
]
