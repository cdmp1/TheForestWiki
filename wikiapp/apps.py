'''from django.apps import AppConfig


class WikiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wikiapp' '''

from django.apps import AppConfig
from django.contrib.auth.models import User

class WikiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wikiapp'

    def ready(self):
        self.crear_admin()

    def crear_admin(self):
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'test123')


