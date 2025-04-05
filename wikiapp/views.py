from django.shortcuts import render

def animales_view(request):
    return render(request, 'Animales.html')

def armas_view(request):
    return render(request, 'Armas.html')

def construcciones_view(request):
    return render(request, 'Construcciones.html')

def consumibles_view(request):
    return render(request, 'Consumibles.html')

def enemigos_view(request):
    return render(request, 'Enemigos.html')

def flora_view(request):
    return render(request, 'Flora.html')

def forowiki_view(request):
    return render(request, 'Forowiki.html')

def historia_view(request):
    return render(request, 'Historia.html')

def inicio_sesion_view(request):
    return render(request, 'Inicio_sesion_wiki.html')

def logros_view(request):
    return render(request, 'Logros.html')

def lugares_view(request):
    return render(request, 'Lugarestf.html')

def menu_principal_view(request):
    return render(request, 'Menu_principal_wiki.html')

def micuenta_view(request):
    return render(request, 'Micuentatf.html')

def recuperarcontra_view(request):
    return render(request, 'Recuperarcontra.html')

def registrarse_view(request):
    return render(request, 'Registrarse_wiki.html')