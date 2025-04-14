from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from .forms import RegistroUsuarioForm
from .models import UsuariosRegistro
from .iniciar_sesion_funcion import iniciar_sesion_wiki

from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm
from django.contrib import messages


# Decorador para vistas de administrador
def solo_admin(user):
    return user.is_authenticated and user.is_staff


# Vistas protegidas por rol admin
@user_passes_test(solo_admin, login_url='/inicio_sesion_wiki/')
def admin_view(request):
    return render(request, 'administrador.html')

@user_passes_test(solo_admin, login_url='/inicio_sesion_wiki/')
def g_foro_view(request):
    return render(request, 'g_foro.html')

@user_passes_test(solo_admin, login_url='/inicio_sesion_wiki/')
def g_secciones_view(request):
    return render(request, 'g_secciones.html')

@user_passes_test(solo_admin, login_url='/inicio_sesion_wiki/')
def g_usuarios_view(request):
    return render(request, 'g_usuarios.html')

@user_passes_test(solo_admin, login_url='/inicio_sesion_wiki/')
def g_web_view(request):
    return render(request, 'g_web.html')


# Vistas públicas generales
def inicio_sesion_wiki(request):
    return render(request, 'Inicio_sesion_wiki.html')

def registrarse_view(request):
    return render(request, 'Registrarse_wiki.html')

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

def logros_view(request):
    return render(request, 'Logros.html')

def lugares_view(request):
    return render(request, 'Lugarestf.html')

def micuenta_view(request):
    return render(request, 'Micuentatf.html')

def recuperarcontra_view(request):
    return render(request, 'Recuperarcontra.html')


# Vista principal con imágenes
def menu_principal_view(request):
    context = {
        'image_paths_animales': [
            'img/imagenes/Animales/1.png', 'img/imagenes/Animales/2.png',
            'img/imagenes/Animales/3.png', 'img/imagenes/Animales/4.png',
            'img/imagenes/Animales/5.png', 'img/imagenes/Animales/6.png',
            'img/imagenes/Animales/7.png', 'img/imagenes/Animales/8.png',
            'img/imagenes/Animales/9.png', 'img/imagenes/Animales/10.png',
            'img/imagenes/Animales/11.png', 'img/imagenes/Animales/12.png',
            'img/imagenes/Animales/13.png',
        ],
        'image_paths_lugares': [
            'img/imagenes/Historia/h1.jpg', 'img/imagenes/Historia/h2.jpg',
            'img/imagenes/Historia/h4.jpg',
        ],
        'image_paths_enemigos': [
            'img/imagenes/Enemigos/Armsy.webp', 'img/imagenes/Enemigos/BabyMutant.webp',
            'img/imagenes/Enemigos/Cowman.webp', 'img/imagenes/Enemigos/DynamiteCannibal.webp',
            'img/imagenes/Enemigos/Girl.webp', 'img/imagenes/Enemigos/Worm.webp',
        ],
        'image_paths_construccion': [
            'img/imagenes/Construcciones/AlpineTreeHouse.webp', 'img/imagenes/Construcciones/AnimalTrap.webp',
            'img/imagenes/Construcciones/BasicFire.webp', 'img/imagenes/Construcciones/FirePit.webp',
            'img/imagenes/Construcciones/Gazebo.webp', 'img/imagenes/Construcciones/RabbitCage.webp',
        ],
        'image_paths_flora': [
            'img/imagenes/Flora/f1.png', 'img/imagenes/Flora/f2.png', 'img/imagenes/Flora/f3.png',
            'img/imagenes/Flora/f4.png', 'img/imagenes/Flora/f5.png', 'img/imagenes/Flora/f6.png',
            'img/imagenes/Flora/f7.png', 'img/imagenes/Flora/f8.png', 'img/imagenes/Flora/f9.png',
        ],
        'image_paths_armas': [
            'img/imagenes/Armas/Arm.webp', 'img/imagenes/Armas/Arrow.webp', 'img/imagenes/Armas/Bomb.webp',
            'img/imagenes/Armas/Bone.webp', 'img/imagenes/Armas/Club.webp', 'img/imagenes/Armas/Chainsaw.webp',
            'img/imagenes/Armas/Crossbow.webp', 'img/imagenes/Armas/Dynamite.webp', 'img/imagenes/Armas/FireArrow.webp',
        ],
        'image_paths_consumibles': [
            'img/imagenes/Consumibles/Aloe.webp', 'img/imagenes/Consumibles/BlackBerries.webp',
            'img/imagenes/Consumibles/Bloodied.webp', 'img/imagenes/Consumibles/Booze.webp',
            'img/imagenes/Consumibles/FishEdible.webp', 'img/imagenes/Consumibles/IconMeatBurnt.webp',
            'img/imagenes/Consumibles/Meat.webp', 'img/imagenes/Consumibles/RabbitMeat.webp',
        ],
        'image_paths_historia': [
            'img/imagenes/Fondos/Fondo4.jpg', 'img/imagenes/Fondos/Fondo5.jpg',
        ],
    }
    return render(request, 'Menu_principal_wiki.html', context)


# Registro de usuario
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            email = form.cleaned_data['email']
            nombre_completo = form.cleaned_data['nombre']
            contraseña = form.cleaned_data['contraseña']

            try:
                usuario = UsuariosRegistro(
                    nombre_usuario=nombre_usuario,
                    email=email,
                    nombre=nombre_completo,
                    contraseña=contraseña
                )
                usuario.save()
                messages.success(request, "Usuario registrado con éxito!")
                return redirect('Menu_principal_wiki')
            except Exception as e:
                form.add_error(None, f"Ocurrió un error al crear la cuenta: {e}")
        # Si no es válido o hubo error
        return render(request, 'Registrarse_wiki.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'Registrarse_wiki.html', {'form': form})


# Cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('inicio_sesion_wiki')


# Editar perfil
@login_required
def editar_perfil(request):
    # Obtener el perfil del usuario autenticado
    try:
        usuario = UsuariosRegistro.objects.get(nombre_usuario=request.user.username)
    except UsuariosRegistro.DoesNotExist:
        messages.error(request, "No se encontró el usuario.")
        return redirect('menu_principal_view')  

    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=usuario)  # Rellenar con los datos actuales del usuario
        if form.is_valid():
            form.save()  # Guardar los cambios
            messages.success(request, 'Tu perfil ha sido actualizado correctamente.')
            return redirect('micuenta_view')  # Redirigir a mi cuenta
    else:
        form = EditarPerfilForm(instance=usuario)  # Rellenar con los datos actuales del usuario

    return render(request, 'editar_perfil.html', {'form': form})
