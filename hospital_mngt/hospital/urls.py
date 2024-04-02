from django.urls import path
from .views import (
    Login,
    logOut_admin,
    Index,
    sofor_goruntule,
    sofor_sil,
    soforEkle,
    arac_goruntule,
    aracEkle,
    atama_goruntule,
    atama_ekle,
    atama_sil,
    arac_sil,
    puantaj_goruntule,
    puantaj_ekle,
    puantaj_sil,
    grafik_view,
    plaka_view
)  # puantaj_ekle import edildi
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", Login, name="admin_login"),
    path("logout/", logOut_admin, name="admin_logout"),
    path("index/", Index, name="dashboard"),
    path("sofor_goruntule/", sofor_goruntule, name="sofor_goruntule"),
    path("atama_goruntule/", atama_goruntule, name="atama_goruntule"),
    path("arac_goruntule/", arac_goruntule, name="arac_goruntule"),
    path("puantaj_goruntule/", puantaj_goruntule, name="puantaj_goruntule"),
    path(
        "puantaj_ekle/", puantaj_ekle, name="puantaj_ekle"
    ),  #! puantaj_ekle URL'i eklendi
    path('grafik/',grafik_view, name='grafik_view'),
    path('plaka/',plaka_view, name='plaka_tablo'),
    path("soforEkle/", soforEkle, name="soforEkle"),
    path("arac_ekle/", aracEkle, name="arac_ekle"),
    path("atama_ekle/", atama_ekle, name="atama_ekle"),
    path("sofor_sil/(?P<pid>\d+)/", sofor_sil, name="sofor_sil"),
    path("atama_sil<int:atama_id>/", atama_sil, name="atama_sil"),
    path("arac_sil<int:pid>/", arac_sil, name="arac_sil"),
    path('puantaj_sil/<int:puantaj_id>/',puantaj_sil, name='puantaj_sil'),
   
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
