from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from ilan.models import *
from django.contrib.auth import get_user_model
User = get_user_model()
Ilanlar = Ilan.objects.filter(durum=True, firma__durum=True, firma__uye__is_active=True).order_by('-id')

### ANASAYFA
def frontpage(request):
    if request.user.is_authenticated == True and request.user.uye_tipi == "is_veren": return redirect('istekler')
    items  = Ilanlar.all()
    title = "En son yayınlanan iş ilanları"
    datas = {
        'head_title': title,
        'page_title': title,
        'items': items,
        'total': items.count()
    }
    return render(request, 'index.html', datas)

### ÜYE KAYIT SAYFASI
def register(request):
    if request.user.is_authenticated: return redirect('frontpage')
    form = HizliKayitFormu(request.POST or None, request.FILES or None)
    if form.is_valid():
        try:
            user = form.save()
            login( request, user )
            messages.success(request, 'Başarıyla kayıt oldunuz, Lütfen profilinizi güncelleyiniz.')
            return redirect('profil')
        except Exception:
            messages.error(request, 'Kayıt olma esnasında bir sorun oluştu.')
            return redirect( 'kayit_ol' )
    datas = { 'form':form, 'head_title': 'Yeni bir iş için kayıt ol' }
    return render(request, 'pages/register-fast.html', datas)




### FİRMA KAYIT SAYFASI
def register_firma(request):
    if request.user.is_authenticated: return redirect('frontpage')
    form = HizliKayitFormu(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        try:
            user = form.save(commit=False)
            user.uye_tipi = 'is_veren'
            user.save()
            login( request, user )
            firma_adi = "Firma %s" % (user.username)
            firma = Firma.objects.create(uye=user, adi=firma_adi, eposta=user.email)
            messages.success(request, 'Başarıyla kayıt oldunuz, Lütfen firma bilgilerini güncelleyiniz.')
            return redirect('firma_duzenle')
        except Exception:
            messages.error(request, 'Kayıt olma esnasında bir sorun oluştu.')
            return redirect( 'kayit_ol_firma' )

    datas = { 'form':form}
    return render(request, 'pages/register-firma.html', datas)

### ÜYE GİRİŞ SAYFASI
def user_login(request):
    if request.user.is_authenticated: return redirect('frontpage')
    form = UyeGirisFormu(request.POST or None)
    datas = { 'form': form }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        next_url = request.GET.get('next', None)
        if next_url and "cikis-yap" in next_url: next_url = None
        user_lin = authenticate(username=username, password=password)
        if user_lin is None:
            messages.error(request, "Giriş Başarısız!.")
            return redirect( 'giris_yap' )
        else:
            login(request, user_lin)
            if next_url is None:
                return redirect( 'frontpage' )
            else:
                return redirect( next_url )
    return render(request, 'pages/login.html', datas)

### ÇIKIŞ YAP
@login_required(login_url='giris_yap')
def user_logout(request):
    logout( request )
    return redirect( 'frontpage' )
