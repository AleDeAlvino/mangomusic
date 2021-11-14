from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from django.shortcuts import get_list_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from .models import Generos, Artistas, Albumes, Canciones
# from .forms import GenerosForm, ArtistaForm, AlbumesForm, CancionesForm

# Create your views here.

@login_required
def configuracion_view(request):
    return render(request, 'configuracion.html')

@login_required
def crud_view(request, model_id):
    return render(request, 'CRUD.html', {'model_id':model_id})

@login_required
def add_canciones_view(request):
    if request.method == 'POST':
        print("holi")
        print("Es valido")
        album = Albumes.objects.filter(pk=request.POST['fk_album']).first()
        genero = Generos.objects.filter(pk=request.POST['fk_genero']).first()
        cancion = Canciones(fk_album=album, fk_genero=genero, cancion=request.POST['cancion'], reproducciones=request.POST['reproducciones'], duracion=request.POST['duracion'])
        cancion.save()
    else:
        print("no entra")
        print(request.method)
    return render(request, 'agregar_canciones.html')

@login_required
def add_artistas_view(request):
    if request.method == 'POST':
        print("holi")
        print("Es valido")
        artista = Artistas(artista=request.POST['artista'], seguidores=request.POST['seguidores'], verificacion=request.POST['verificacion'], foto=request.FILES['foto'])
        artista.save()
    else:
        print("no entra")
        print(request.method)
    return render(request, 'agregar_artistas.html')

@login_required
def add_albumes_view(request):
    if request.method == 'POST':
        print("holi")
        print("Es valido")
        artista = Artistas.objects.filter(pk=request.POST['fk_artista']).first()
        album = Albumes(fk_artista=artista, album=request.POST['album'], fecha=request.POST['fecha'], foto=request.FILES['foto'])
        album.save()
    else:
        print("no entra")
        print(request.method)
    return render(request, 'agregar_albumes.html')

@login_required
def add_generos_view(request):
    if request.method == 'POST':
        print("holi")
        print("Es valido")
        genero = Generos(genero=request.POST['genero'])
        genero.save()
    else:
        print("no entra")
        print(request.method)
    return render(request, 'agregar_generos.html')


# Modificar el html al correspondiente
@login_required
def artistas_view(request):
    return render(request, 'agregar_artistas.html')