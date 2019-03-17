from django.utils.text import slugify
import datetime
from django.conf import settings
from datetime import timedelta
from django.utils import timezone
from django.shortcuts import redirect

def son_x_gun(gun=1):
    return timezone.now().date() - timedelta(days=gun)

def get_slug(title):
    return slugify(title.replace('Ş','S').replace('ı', 'i'))



def asw_unique_slug(instance, title):
    Klass = instance.__class__
    new_slug, counter = get_slug(title), 0
    while Klass.objects.filter(slug=new_slug).exclude(pk=instance.id).exists()==True:
        counter += 1
        new_slug = "{}-{}".format( new_slug, str(counter) )
    return new_slug


def set_cookie(response, key, value, days_expire = 7):
  if days_expire is None:
    max_age = 365 * 24 * 60 * 60  #one year
  else:
    max_age = days_expire * 24 * 60 * 60
  expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
  response.set_cookie(key, value, max_age=max_age, expires=expires, domain=settings.SESSION_COOKIE_DOMAIN, secure=settings.SESSION_COOKIE_SECURE or None)



def get_youtube_id(url=None):
    result = url.split('?v=')[1]
    result = result.split('&')[0]
    return result



def get_youtube_embed_url(url=None):
    id = get_youtube_id(url)
    result = "https://www.youtube.com/embed/{}".format( str(id) )
    return result

def notBoss(request):
    islem = False
    if request.user.is_authenticated == False:
        islem = True
    if request.user.is_authenticated == True and request.user.uye_tipi != "is_veren":
        islem = True
    return islem
