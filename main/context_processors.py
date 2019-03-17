from system.models import Zaman, Sehir, Meslek
from datetime import timedelta
from django.utils import timezone
from django.db.models import Count

bugun = timezone.datetime.now()

def dakikada_contents(request):
    return {
        "globalZamanList": Zaman.objects.all(),
        "globalSehirList": Sehir.objects.filter(ilan__durum=True, ilan__firma__durum=True, ilan__firma__uye__is_active=True).annotate(ilan_sayisi=Count('ilan__item')).order_by('-ilan_sayisi')[:40],
        "globalMeslekList": Meslek.objects.filter(ilan__durum=True, ilan__firma__durum=True, ilan__firma__uye__is_active=True).annotate(ilan_sayisi=Count('ilan__item')).order_by('-ilan_sayisi')[:23],
        "globalSehirListIstek": Sehir.objects.filter(istek__durum=True, istek__uye__is_active=True).annotate(istek_sayisi=Count('istek__item')).order_by('-istek_sayisi')[:40],
        "globalMeslekListIstek": Meslek.objects.filter(istek__durum=True, istek__uye__is_active=True).annotate(istek_sayisi=Count('istek__item')).order_by('-istek_sayisi')[:23]
    }


def dakikada_get_socials(request):
    datas = [
        {   'tag'   : 'fb',
            'class' : 'fab fa-facebook-f',
            'title' : 'Facebook sayfamızı beğen',
            'url'   : '' },

        {   'tag'   : 'tt',
            'class' : 'fab fa-twitter',
            'title' : 'Twitter\'da takip edin',
            'url'   : '' },

        {   'tag'   : 'in',
            'class' : 'fab fa-instagram',
            'title' : 'İnstagram hesabımız',
            'url'   : '' },

        {   'tag'   : 'yt',
            'class' : 'fab fa-youtube',
            'title' : 'Youtube\'dan izleyin',
            'url'   : '' },

        {   'tag'   : 'pi',
            'class' : 'fab fa-pinterest-p',
            'title' : 'Pinterestten takip edin',
            'url'   : '' },

        {   'tag'   : 'gp',
            'class' : 'fab fa-google-plus-g',
            'title' : 'Google+ Hesabımız',
            'url'   : '' },
    ]
    return {
        'dakikada_socials': datas
    }
