from django.db import models
from django.contrib.auth.hashers import make_password

# Modelo base de la tabla de django 
class UsuariosRegistro(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=128) 

    def save(self, *args, **kwargs):
        # Hashea la contraseña antes de guardar
        self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)
