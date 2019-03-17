from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import logout, login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from ilan.models import Istek, Firma

def lc(obj, limit):
    return len(str(obj)) < limit


################################################################################
@login_required(login_url='giris_yap')
def user_logout(request):
    logout( request )
    return redirect( 'frontpage' )


################################################################################
@login_required(login_url='login')
def sifre_degistir(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Kullanıcı şifreniz başarıyla değiştirildi.")
            return redirect('sifre_degistir')
        else:
            messages.error(request, "Kullanıcı şifreniz değiştirilemedi")
    else:
        form = PasswordChangeForm(request.user)

    datas = {
        'head_title': "Şifre Değiştir",
        'form': form
    }
    return render(request, "user/sifre.html", datas)


################################################################################
################################################################################
################################################################################

################################################################################
@login_required(login_url="giris_yap")
def duzenle(request):
    user = User.objects.get(pk=request.user.id)
    form = UyeGuncellemeFormu(request.POST or None, request.FILES or None, instance=user)
    if request.method == "POST" and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Bilgileriniz başarılı bir şekilde güncellendi.')
        except Exception:
            messages.error(request, 'Bilgiler güncellenirken bir sorun oluştu. Lütfen tekrar deneyin.')
        return redirect( 'hesap' )
    datas = { 'form':form, 'head_title': "Profil bilgilerini güncelle" }
    return render(request, 'user/profile-edit.html', datas)


@login_required(login_url="giris_yap")
def duzenle_firma(request):
    try:
        firma = Firma.objects.get(uye=request.user)
    except:
        firma_adi = "Firma %s" % (request.user.username)
        firma = Firma.objects.create( uye=request.user, adi=firma_adi, eposta=request.user.email )
        return redirect('firma_duzenle')


    form = FirmaGuncellemeFormu(request.POST or None, request.FILES or None, instance=firma)
    if request.method == "POST" and form.is_valid():
        try:
            form.save()
            messages.success(request, 'Firma bilgileriniz başarılı bir şekilde güncellendi.')
        except Exception:
            messages.error(request, 'Bilgiler güncellenirken bir sorun oluştu. Lütfen tekrar deneyin.')
        return redirect( 'firma_duzenle' )
    datas = { 'form':form, 'head_title': "Firma bilgilerini güncelle" }
    return render(request, 'user/firm-edit.html', datas)



################################################################################
################################################################################
################################################################################

################################################################################
@login_required(login_url='giris_yap')
def isteklerim(request):
    if request.user.uye_tipi != "kullanici": return redirect('frontpage')
    istekler = Istek.objects.filter(uye=request.user).order_by('-id')
    datas = { 'items': istekler, 'head_title': 'İş İsteklerim' }
    return render(request, 'user/isteklerim.html', datas)




################################################################################
@login_required(login_url='giris_yap')
def istek_olustur(request):
    if request.user.uye_tipi != "kullanici": return redirect('frontpage')
    form = IsIstegiForm(request.POST or None)
    datas = { 'form': form, 'head_title': 'İş isteği oluştur' }
    if form.is_valid():
        try:
            istek = form.save(commit=False)
            istek.durum = request.POST.get('durum', 0)
            istek.uye = request.user
            istek.save()
            form.save_m2m()
            return redirect("isteklerim")
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
    return render(request, 'user/istek-olustur.html', datas)



@login_required(login_url='giris_yap')
def istek_duzenle(request, id):
    if request.user.uye_tipi != "kullanici": return redirect('frontpage')
    istek = get_object_or_404(Istek, pk=id, uye=request.user)
    form = IsIstegiForm(request.POST or None, instance=istek)
    datas = { 'form': form, 'head_title': 'İş isteğini düzenle' }
    if form.is_valid():
        try:
            istek = form.save(commit=False)
            istek.durum = request.POST.get('durum', 0)
            istek.save()
            form.save_m2m()
            return redirect( istek.get_edit_url() )
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
    return render(request, 'user/istek-olustur.html', datas)


@login_required(login_url='giris_yap')
def istek_sil(request, id):
    if request.user.uye_tipi != "kullanici": return redirect('frontpage')
    istek = get_object_or_404(Istek, pk=id, uye=request.user)
    datas = { 'item': istek, 'head_title': 'İş isteğini sil' }
    if request.method == "POST" and request.POST.get("islem", False) == "sil":
        try:
            istek.delete()
            messages.success(request, "İsteğiniz başarılı bir şekilde silindi.")
            return redirect("isteklerim")
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
    return render(request, 'user/istek-sil.html', datas)

################################################################################
################################################################################
################################################################################

################################################################################
@login_required(login_url='giris_yap')
def ilanlarim(request):
    if request.user.uye_tipi != "is_veren": return redirect('frontpage')
    firma = Firma.objects.filter(uye=request.user).first()
    ilanlar = Ilan.objects.filter(firma=firma).order_by('-id')
    datas = { 'items': ilanlar, 'head_title': 'İş İlanlarım' }
    return render(request, 'user/ilanlarim.html', datas)




################################################################################
@login_required(login_url='giris_yap')
def ilan_olustur(request):
    if request.user.uye_tipi != "is_veren": return redirect('is_istegi_olustur')
    if not request.user.is_authenticated: return redirect('kayit_ol_firma')
    f = Firma.objects.filter(uye=request.user).first()
    form = IlanForm(request.POST or None)

    datas = { 'form': form, 'firma': f }

    if form.is_valid():
        try:
            ilan = form.save(commit=False)
            ilan.firma = f
            ilan.save()
            form.save_m2m()
            return redirect("ilanlarim")
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
    return render(request, 'user/ilan-olustur.html', datas)


@login_required(login_url='giris_yap')
def ilan_duzenle(request, id=None):
    if request.user.uye_tipi != "is_veren": return redirect('is_istegi_olustur')
    if not request.user.is_authenticated: return redirect('kayit_ol_firma')
    f = Firma.objects.filter(uye=request.user).first()
    ilan = get_object_or_404(Ilan, pk=id, firma=request.user.firma)
    form = IlanForm(request.POST or None, instance=ilan)

    datas = { 'form': form, 'firma': f }

    if form.is_valid():
        try:
            ilan = form.save(commit=False)
            ilan.save()
            form.save_m2m()
            return redirect( ilan.get_edit_url() )
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")
    return render(request, 'user/ilan-olustur.html', datas)

@login_required(login_url='giris_yap')
def ilan_sil(request, id=None):
    if request.user.uye_tipi != "is_veren": return redirect('is_istegi_olustur')
    if not request.user.is_authenticated: return redirect('kayit_ol_firma')
    ilan = get_object_or_404(Ilan, pk=id, firma=request.user.firma)
    datas = { 'item': ilan }
    if request.method == "POST" and request.POST.get("islem", False) == "sil":
        try:
            ilan.delete()
            messages.success(request, "İlanınız başarılı bir şekilde silindi.")
            return redirect("ilanlarim")
        except:
            messages.warning(request, "Bir sorun oluştu. Lütfen daha sonra tekrar deneyin.")

    return render(request, 'user/ilan-sil.html', datas)












##############################################
