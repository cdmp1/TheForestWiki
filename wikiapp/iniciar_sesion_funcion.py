from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django import forms

def iniciar_sesion_wiki(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Menu_principal_wiki')  # Redirige a la página principal después del inicio de sesión
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
    else:
        form = InicioSesionForm()
    return render(request, 'Inicio_sesion_wiki.html', {'form': form})