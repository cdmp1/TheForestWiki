

from django.db import models

#Modelo que es la base dde la tabla que usa django 
class UsuariosRegistro(models.Model):
    nombre_usuario = models.CharField(max_length=30, unique=True)
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, unique=True)
    contraseña = models.CharField(max_length=12)

    def __str__(self):
        return self.nombre_usuario 