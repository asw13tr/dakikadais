from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('ilanlar/istek/<int:id>', uygun_ilanlar, name='uygun_ilanlar'),
    path('<slug:slug>-<int:id>-<slug:sehir>-is-ilani', ilan_detay, name='ilan_detay'),
    path('is-ara', ilan_ara, name='ilan_ara'),
    path('<slug:sehir>-is-ilanlari-sehir-<int:id>', ilan_ara_sehir, name='ilan_ara_sehir'),
    path('<slug:meslek>-is-ilanlari-meslek-<int:id>', ilan_ara_meslek, name='ilan_ara_meslek'),
    path('<slug:zaman>-is-ilanlari-mesai-<int:id>', ilan_ara_zaman, name='ilan_ara_zaman'),

    path('istekler', istekler, name='istekler'),
    path('istek-ara', istek_ara, name='istek_ara'),
    path('istekler/ilan/<int:id>', uygun_istekler, name='uygun_istekler'),
    path('istekler/<slug:meslek>-meslek-<int:id>', istek_ara_meslek, name='istek_ara_meslek'),
    path('istekler/<slug:sehir>-sehir-<int:id>', istek_ara_sehir, name='istek_ara_sehir'),
    path('istek/<slug:slug>-<int:id>', istek_detay, name='istek_detay'),
]
