from django.urls import path
from . import views

urlpatterns = [
    path('animales/', views.animales_view, name='animales'),
    path('armas/', views.armas_view, name='armas'),
    path('construcciones/', views.construcciones_view, name='construcciones'),
    path('consumibles/', views.consumibles_view, name='consumibles'),
    path('enemigos/', views.enemigos_view, name='enemigos'),
    path('flora/', views.flora_view, name='flora'),
    path('forowiki/', views.forowiki_view, name='forowiki'),
    path('historia/', views.historia_view, name='historia'),
    path('inicio_sesion/', views.inicio_sesion_view, name='inicio_sesion'),
    path('logros/', views.logros_view, name='logros'),
    path('lugares/', views.lugares_view, name='lugares'),
    path('Menu_principal_wiki/', views.menu_principal_view, name='Menu_principal_wiki'),
    path('micuenta/', views.micuenta_view, name='micuenta'),
    path('recuperarcontra/', views.recuperarcontra_view, name='recuperarcontra'),
    path('registrarse/', views.registrarse_view, name='registrarse'),
]
