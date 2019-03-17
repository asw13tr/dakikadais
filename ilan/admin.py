from django.contrib import admin
from .models import *

class AdminModel(admin.ModelAdmin):

    list_display = ('durum','adi','yetkili',)
    list_display_links = ['adi']

    class Meta:
        model = Firma

class AdminIlan(admin.ModelAdmin):

    list_display = ('durum','baslik',)
    list_display_links = ['baslik']

    class Meta:
        model = Ilan

class AdminIstek(admin.ModelAdmin):

    list_display = ('durum','baslik','uye','meslek',)
    list_display_links = ['baslik']

    class Meta:
        model = Istek

admin.site.register(Firma, AdminModel)
admin.site.register(Ilan, AdminIlan)
admin.site.register(Istek, AdminIstek)
