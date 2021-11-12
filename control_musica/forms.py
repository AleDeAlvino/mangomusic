from django import forms
from .models import Generos, Artistas, Albumes, Canciones

# Falta cambiar los campos de artista, albumnes y canciones

class GenerosForm(forms.ModelForm):
    """ Formulario para registrar un Genero """

    class Meta:
        model = Generos
        fields=('genero')

class ArtistaForm(forms.ModelForm):
    """ Formulario para registrar un Artista """

    class Meta:
        model = Generos
        fields=('genero','last_name', 'first_name', 'pais', 'fecha_nac', 'password')

class AlbumesForm(forms.ModelForm):
    """ Formulario para registrar un Album """

    class Meta:
        model = Generos
        fields=('genero','last_name', 'first_name', 'pais', 'fecha_nac', 'password')

class CancionesForm(forms.ModelForm):
    """ Formulario para registrar una Cancion """

    class Meta:
        model = Generos
        fields=('genero','last_name', 'first_name', 'pais', 'fecha_nac', 'password')