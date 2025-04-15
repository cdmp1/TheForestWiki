from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Crea el superusuario y lo asigna al grupo Administrador si no existe.'

    def handle(self, *args, **kwargs):
        group, _ = Group.objects.get_or_create(name='Administrador')

        if not User.objects.filter(username='admin').exists():
            user = User.objects.create_superuser('admin', 'admin@example.com', 'test123')
            user.groups.add(group)
            self.stdout.write(self.style.SUCCESS("Superusuario 'admin' creado y agregado al grupo 'Administrador'."))
        else:
            self.stdout.write(self.style.WARNING("El superusuario 'admin' ya existe."))
