from django.contrib import admin
from django.urls import path, include
import system.views as v_system
from django.conf.urls.static import static
from django.conf import settings
import main.views as v_main
import ilan.views as v_ilan
import user.urls
import ilan.urls


urlpatterns = [
    path('dakikadapanel/', admin.site.urls),
    #path('veritabanini_doldur', v_system.veritabanini_doldur, name="veritabanini_doldur"),
    path('', include(ilan.urls)),
    path('', v_main.frontpage, name='frontpage' ),
    path('hesap/', include(user.urls)),
    path('cikis-yap', v_main.user_logout, name='cikis_yap' ),
    path('giris-yap', v_main.user_login, name='giris_yap' ),
    path('kayit-ol', v_main.register, name='kayit_ol' ),
    path('kayit-ol-firma', v_main.register_firma, name='kayit_ol_firma' ),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
