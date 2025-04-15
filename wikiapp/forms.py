from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
import re
from .models import UsuariosRegistro


# Función de validación para asegurar que el nombre de usuario no esté repetido
def username_no_repetido_validator(value, user=None):
    if user is None:
        if User.objects.filter(username=value).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
    else:
        # En la edición, verificamos que el nombre de usuario no sea usado por otro
        if User.objects.filter(username=value).exclude(id=user.id).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")

# Función de validación para asegurar que el correo electrónico no esté repetido
def email_no_repetido_validator(value, user=None):
    if user is None:
        if User.objects.filter(email=value).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")
    else:
        # En la edición, verificamos que el correo no esté siendo usado por otro
        if User.objects.filter(email=value).exclude(id=user.id).exists():
            raise forms.ValidationError("Este correo electrónico ya está registrado.")

# Validador que asegura el uso exclusivo de letras y espacios
class SoloLetrasEspaciosValidator:
    def __call__(self, value):
        if not re.match(r'^[a-zA-Z\s]+$', value):
            raise forms.ValidationError("El nombre solo puede contener letras y espacios.")

# Validador que asegura que la contraseña contenga al menos un carácter especial
class PasswordSymbolValidator:
    def __call__(self, value):
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial.")

# Formulario de registro de usuario


class RegistroUsuarioForm(forms.Form):
    nombre_usuario = forms.CharField(
        max_length=30,
        required=True,
        label='Nombre de Usuario',
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        validators=[MinLengthValidator(2, "El nombre de usuario debe tener al menos 2 caracteres."),
                    MaxLengthValidator(15, "El nombre de usuario no puede tener más de 15 caracteres.")]
    )

    nombre = forms.CharField(
        required=True,
        label='Nombre Completo',
        max_length=30,
        validators=[MinLengthValidator(2, "El nombre debe tener al menos 2 caracteres."),
                    SoloLetrasEspaciosValidator()]
    )

    email = forms.EmailField(
        required=True,
        label='Correo Electrónico',
        max_length=50,
    )

    contraseña = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label='Contraseña',
        validators=[MinLengthValidator(6, "La contraseña debe tener al menos 6 caracteres."),
                    MaxLengthValidator(12, "La contraseña no puede tener más de 12 caracteres."),
                    PasswordSymbolValidator()]
    )

    confirmar_contraseña = forms.CharField(
        widget=forms.PasswordInput,
        required=True,
        label='Confirmar Contraseña'
    )

    # Método de limpieza para comparar las contraseñas
    def clean(self):
        cleaned_data = super().clean()
        contraseña = cleaned_data.get("contraseña")
        confirmar_contraseña = cleaned_data.get("confirmar_contraseña")

        # Verificar si las contraseñas coinciden
        if contraseña and confirmar_contraseña and contraseña != confirmar_contraseña:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data




