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
        model = Artistas
        fields=('artista','seguidores', 'verificacion')

class AlbumesForm(forms.ModelForm):
    """ Formulario para registrar un Album """

    class Meta:
        model = Albumes
        fields=('fk_artista','album', 'fecha')

class CancionesForm(forms.ModelForm):
    """ Formulario para registrar una Cancion """

    class Meta:
        model = Canciones
        fields=('fk_album','fk_genero', 'cancion', 'reproducciones', 'duracion')