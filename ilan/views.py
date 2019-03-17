from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import *
from system.models import *
from main.functions import notBoss
from datetime import datetime

Ilanlar = Ilan.objects.filter(durum=True, firma__durum=True, firma__uye__is_active=True).order_by('-id')
Istekler = Istek.objects.filter(durum=True, uye__is_active=True).order_by('-id')

def ilan_detay(request, slug, id, sehir):
    ilan = get_object_or_404(Ilan, pk=id, durum=True)
    page_title = "%s %s iş ilanı" % ( ilan.baslik, ilan.sehir.isim )
    datas = {'item':ilan, 'head_title':page_title, 'page_title':page_title }
    return render(request, 'show.html', datas)

def ilan_ara_sehir(request, sehir, id):
    sehir = get_object_or_404(Sehir, pk=id)
    ilanlar = Ilanlar.filter( sehir=sehir )
    page_title = "%s iş ilanları" % (sehir.isim)
    datas = {'items':ilanlar, 'head_title':page_title, 'page_title':page_title, 'total':ilanlar.count() }
    return render(request, "index.html", datas)

def ilan_ara_meslek(request, meslek, id):
    meslek = get_object_or_404(Meslek, pk=id)
    ilanlar = Ilanlar.filter(meslek=meslek)
    page_title = "%s iş ilanları" % (meslek.baslik)
    datas = {'items':ilanlar, 'head_title':page_title, 'page_title':page_title, 'total':ilanlar.count() }
    return render(request, "index.html", datas)

def ilan_ara_zaman(request, zaman, id):
    zaman = get_object_or_404(Zaman, pk=id)
    ilanlar = Ilanlar.filter( zaman=zaman )
    page_title = "%s iş ilanları" % (zaman.baslik)
    datas = {'items':ilanlar, 'head_title':page_title, 'page_title':page_title, 'total':ilanlar.count() }
    return render(request, "index.html", datas)

def ilan_ara(request):
    aranan = request.GET.get("q", False)
    ilanlar = False
    if len(aranan) > 2:
        ilanlar = Ilanlar.filter( Q(baslik__icontains=aranan) | Q(detay__icontains=aranan) )

    if ilanlar == False:
        return redirect("frontpage")
    else:
        page_title = "\"%s\" aramasına ait iş ilanları" % (aranan)
        datas = {'items':ilanlar, 'head_title':page_title, 'page_title':page_title, 'total':ilanlar.count()}
        return render(request, "index.html", datas)

def uygun_ilanlar(request, id):
    istek = get_object_or_404(Istekler, pk=id)
    ilanlar = Ilanlar.filter( Q(sehir=istek.sehir) &
                                Q(meslek__in=[istek.meslek,]) &
                                Q(tecrube__lte=istek.tecrube) &
                                Q(zaman__in=istek.zaman.all()) &
                                Q(maas__in=istek.maas.all()) &
                                Q(egitim__in= [istek.uye.egitim,] ) &
                                Q(dil_konusma__in=istek.uye.dil_konusma.all()) &
                                Q(dil_yazma__in=istek.uye.dil_yazma.all()) &
                                Q(cinsiyet__in=["F", istek.uye.cinsiyet]) &
                                Q(yas_min__lte=istek.uye.get_yas()) & Q(yas_max__gte=istek.uye.get_yas() )
                                )

    if istek.uye.cinsiyet == "E":
        ilanlar = ilanlar.filter( Q(askerlik__in=[istek.uye.askerlik,]) )

    ilanlar = ilanlar.distinct()
    page_title = "%s başlıklı isteğinize uygun ilanlar" % (istek.baslik)
    datas = {'items':ilanlar, 'head_title':page_title, 'page_title':page_title, 'total':ilanlar.count() }
    return render(request, "index.html", datas)




###############################################################################
###############################################################################
###############################################################################
def istekler(request):
    if notBoss(request): return redirect("frontpage")
    items  = Istekler.all()
    title = "En son yayınlanan iş istekleri"
    datas = {
        'head_title': title,
        'page_title': title,
        'items': items,
        'total': items.count()
    }
    return render(request, 'index.html', datas)

def istek_detay(request, slug, id):
    istek = get_object_or_404(Istek, pk=id, durum=True)
    page_title = "%s iş isteği" % ( istek.baslik )
    datas = {'item':istek, 'head_title':page_title, 'page_title':page_title }
    return render(request, 'istek.html', datas)

def istek_ara_meslek(request, meslek, id):
    meslek = get_object_or_404(Meslek, pk=id)
    istekler = Istekler.filter( meslek=meslek )
    page_title = "%s istekleri" % (meslek.baslik)
    datas = {'items':istekler, 'head_title':page_title, 'page_title':page_title, 'total':istekler.count() }
    return render(request, "index.html", datas)

def istek_ara_sehir(request, sehir, id):
    sehir = get_object_or_404(Sehir, pk=id)
    istekler = Istekler.filter( sehir=sehir )
    page_title = "%s istekleri" % (sehir.isim)
    datas = {'items':istekler, 'head_title':page_title, 'page_title':page_title, 'total':istekler.count() }
    return render(request, "index.html", datas)

def istek_ara(request):
    aranan = request.GET.get("q", False)
    istekler = False
    if len(aranan) > 2:
        istekler = Istekler.filter( Q(baslik__icontains=aranan) | Q(detay__icontains=aranan) )

    if istekler == False:
        return redirect("frontpage")
    else:
        page_title = "\"%s\" aramasına ait iş istekleri" % (aranan)
        datas = {'items':istekler, 'head_title':page_title, 'page_title':page_title, 'total':istekler.count()}
        return render(request, "index.html", datas)


def uygun_istekler(request, id):
    ilan = get_object_or_404(Ilan, pk=id)
    nowDate = datetime.now().date()
    min_agedate = datetime(nowDate.year - ilan.yas_min, nowDate.month, nowDate.day).date()
    max_agedate = datetime(nowDate.year - (ilan.yas_max+1), nowDate.month, nowDate.day).date()

    istekler = Istekler.filter( Q(sehir=ilan.sehir) &
                                Q(meslek__in=ilan.meslek.all()) &
                                Q(tecrube__gte=ilan.tecrube) &
                                Q(zaman__in=ilan.zaman.all()) &
                                Q(maas__in=ilan.maas.all()) &
                                Q(uye__egitim__in=ilan.egitim.all()) &
                                Q(uye__dil_konusma__in=ilan.dil_konusma.all()) &
                                Q(uye__dil_yazma__in=ilan.dil_yazma.all()) &
                                Q(uye__dogum_tarihi__lte=min_agedate) & Q(uye__dogum_tarihi__gte=max_agedate) )
    if ilan.cinsiyet != "F":
        istekler = istekler.filter( Q(uye__cinsiyet=ilan.cinsiyet) )

    if ilan.cinsiyet != "K":
        istekler = istekler.filter( Q(uye__askerlik__in=ilan.askerlik.all()) )

    istekler = istekler.distinct()
    page_title = "%s başlıklı ilanınıza uygun istekler" % (ilan.baslik)
    datas = {'items':istekler, 'head_title':page_title, 'page_title':page_title, 'total':istekler.count() }
    return render(request, "index.html", datas)
