

from django.contrib import admin
from .models import UsuariosRegistro

admin.site.register(UsuariosRegistro)


from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User

admin_group, created = Group.objects.get_or_create(name='Administrador')

user = User.objects.get(username='admin')
user.groups.add(admin_group)
