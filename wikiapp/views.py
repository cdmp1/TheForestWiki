from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from .models import UsuariosRegistro  
from django.contrib import messages

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

def inicio_sesion_wiki(request):
    return render(request, 'Inicio_sesion_wiki.html')

def logros_view(request):
    return render(request, 'Logros.html')

def lugares_view(request):
    return render(request, 'Lugarestf.html')

def micuenta_view(request):
    return render(request, 'Micuentatf.html')

def recuperarcontra_view(request):
    return render(request, 'Recuperarcontra.html')

def registrarse_view(request):
    return render(request, 'Registrarse_wiki.html')


from django.shortcuts import render

def menu_principal_view(request):
    image_paths_animales = [
        'img/imagenes/Animales/1.png',
        'img/imagenes/Animales/2.png',
        'img/imagenes/Animales/3.png',
        'img/imagenes/Animales/4.png',
        'img/imagenes/Animales/5.png',
        'img/imagenes/Animales/6.png',
        'img/imagenes/Animales/7.png',
        'img/imagenes/Animales/8.png',
        'img/imagenes/Animales/9.png',
        'img/imagenes/Animales/10.png',
        'img/imagenes/Animales/11.png',
        'img/imagenes/Animales/12.png',
        'img/imagenes/Animales/13.png',
    ]

    image_paths_lugares = [
        'img/imagenes/Historia/h1.jpg',
        'img/imagenes/Historia/h2.jpg',
        'img/imagenes/Historia/h4.jpg',

    ]
    image_paths_enemigos = [
        'img/imagenes/Enemigos/Armsy.webp',
        'img/imagenes/Enemigos/BabyMutant.webp',
        'img/imagenes/Enemigos/Cowman.webp',
        'img/imagenes/Enemigos/DynamiteCannibal.webp',
        'img/imagenes/Enemigos/Girl.webp',
        'img/imagenes/Enemigos/Worm.webp',

    ]
    image_paths_construccion = [
        'img/imagenes/Construcciones/AlpineTreeHouse.webp',
        'img/imagenes/Construcciones/AnimalTrap.webp',
        'img/imagenes/Construcciones/BasicFire.webp',
        'img/imagenes/Construcciones/FirePit.webp',
        'img/imagenes/Construcciones/Gazebo.webp',
        'img/imagenes/Construcciones/RabbitCage.webp',

    ]
    image_paths_flora = [
        'img/imagenes/Flora/f1.png',
        'img/imagenes/Flora/f2.png',
        'img/imagenes/Flora/f3.png',
        'img/imagenes/Flora/f4.png',
        'img/imagenes/Flora/f5.png',
        'img/imagenes/Flora/f6.png',
        'img/imagenes/Flora/f7.png',
        'img/imagenes/Flora/f8.png',
        'img/imagenes/Flora/f9.png',

    ]
    image_paths_armas= [
        'img/imagenes/Armas/Arm.webp',
        'img/imagenes/Armas/Arrow.webp',
        'img/imagenes/Armas/Bomb.webp',
        'img/imagenes/Armas/Bone.webp',
        'img/imagenes/Armas/Club.webp',
        'img/imagenes/Armas/Chainsaw.webp',
        'img/imagenes/Armas/Crossbow.webp',
        'img/imagenes/Armas/Dynamite.webp',
        'img/imagenes/Armas/FireArrow.webp',

    ]
    image_paths_consumibles= [
        'img/imagenes/Consumibles/Aloe.webp',
        'img/imagenes/Consumibles/BlackBerries.webp',
        'img/imagenes/Consumibles/Bloodied.webp',
        'img/imagenes/Consumibles/Booze.webp',
        'img/imagenes/Consumibles/FishEdible.webp',
        'img/imagenes/Consumibles/IconMeatBurnt.webp',
        'img/imagenes/Consumibles/Meat.webp',
        'img/imagenes/Consumibles/RabbitMeat.webp',

    ]

    image_paths_historia= [
        'img/imagenes/Fondos/Fondo4.jpg',
        'img/imagenes/Fondos/Fondo5.jpg',

    ]


    context = {
        'image_paths_animales': image_paths_animales,
        'image_paths_lugares': image_paths_lugares,
        'image_paths_enemigos': image_paths_enemigos,
        'image_paths_construccion': image_paths_construccion,
        'image_paths_flora': image_paths_flora,
        'image_paths_armas': image_paths_armas,
        'image_paths_consumibles': image_paths_consumibles,
        'image_paths_historia': image_paths_historia,
    }
    return render(request, 'Menu_principal_wiki.html', context)


def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            email = form.cleaned_data['email']
            nombre_completo = form.cleaned_data['nombre']
            contraseña = form.cleaned_data['contraseña']

            try:
                # Crea un usuario en la tabla UsuariosRegistro
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
                return render(request, 'registrarse_wiki.html', {'form': form})
        else:
            return render(request, 'registrarse_wiki.html', {'form': form})
    else:
        form = RegistroUsuarioForm()
        return render(request, 'registrarse_wiki.html', {'form': form})