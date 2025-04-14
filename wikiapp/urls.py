from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.menu_principal_view, name='inicio'),

    # Vistas del sitio
    path('animales/', views.animales_view, name='animales'),
    path('armas/', views.armas_view, name='armas'),
    path('construcciones/', views.construcciones_view, name='construcciones'),
    path('consumibles/', views.consumibles_view, name='consumibles'),
    path('enemigos/', views.enemigos_view, name='enemigos'),
    path('flora/', views.flora_view, name='flora'),
    path('forowiki/', views.forowiki_view, name='forowiki'),
    path('historia/', views.historia_view, name='historia'),
    path('logros/', views.logros_view, name='logros'),
    path('lugares/', views.lugares_view, name='lugares'),
    path('micuenta/', views.micuenta_view, name='micuenta'), 
    path('recuperarcontra/', views.recuperarcontra_view, name='recuperarcontra'),

    # Autenticación
    path('inicio_sesion_wiki/', views.inicio_sesion_wiki, name='inicio_sesion_wiki'),
    path('registrarse/', views.registrarse_view, name='registrarse'),

    # Panel administrador
    path('admin/', views.admin_view, name='admin_wiki'),
    path('g_foro/', views.g_foro_view, name='admin_foro'),
    path('g_secciones/', views.g_secciones_view, name='admin_secciones'),
    path('g_usuarios/', views.g_usuarios_view, name='admin_usuarios'),               
    path('g_web/', views.g_web_view, name='admin_web'),
]
