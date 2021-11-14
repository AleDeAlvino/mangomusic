from django import forms
from .models import User

# Arreglar lo de tipo de usuario y campos faltantes

class ProfileForm(forms.ModelForm):
    """ Formulario para registrar un usuario """

    class Meta:
        model = User
        help_texts = {'username': None,}
        fields=('username','last_name', 'first_name', 'pais', 'fecha_nac', 'password')
        widgets = {
            'password':forms.PasswordInput(attrs={'required':True}),
        }

class UserForm(forms.ModelForm):
    """ Formulario para actualizar un usuario """

    class Meta:
        model = User
        help_texts = {'username': None,}
        fields=('username','first_name','last_name','pais','fecha_nac', 'avatar', 'desc')

class BusquedaForm(forms.Form):
    """ Formulario para buscar una Cancion, un Album o Artista """

    class Meta:
        fields=('search',)