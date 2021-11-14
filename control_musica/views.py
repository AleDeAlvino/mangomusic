from django.shortcuts import get_object_or_404, render
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

from control_musica.forms import GenerosForm
from .models import Generos, Artistas, Albumes, Canciones
from .forms import GenerosForm, ArtistaForm, AlbumesForm, CancionesForm

# Create your views here.

@login_required
def configuracion_view(request):
    return render(request, 'configuracion.html')

@login_required
def crud_view(request, model_id):
    return render(request, 'CRUD.html', {'model_id':model_id})

# ---------------- AGREGAR ----------------

@login_required
def add_canciones_view(request):
    if request.method == 'POST':
        print("holi")
        print("Es valido")
        album = Albumes.objects.filter(pk=request.POST['fk_album']).first()
        genero = Generos.objects.filter(pk=request.POST['fk_genero']).first()
        cancion = Canciones(fk_album=album, fk_genero=genero, cancion=request.POST['cancion'], reproducciones=request.POST['reproducciones'], duracion=request.POST['duracion'], link=request.POST['link'])
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

# ---------------- MOSTRAR ----------------

@login_required
def m_generos_view(request):
    generos = Generos.objects.all()
    return render(request, 'mostrar_generos.html', {'generos':generos})

@login_required
def m_artistas_view(request):
    artistas = Artistas.objects.all()
    return render(request, 'mostrar_artistas.html', {'artistas':artistas})

@login_required
def m_albumes_view(request):
    albumes = Albumes.objects.all()
    return render(request, 'mostrar_albumes.html', {'albumes':albumes})

@login_required
def m_canciones_view(request):
    canciones = Canciones.objects.all()
    return render(request, 'mostrar_canciones.html', {'canciones':canciones})

# ---------------- DELETES ----------------
@login_required
def d_generos_view(request, genero_id):
    genero = get_object_or_404(Generos, id= genero_id)
    genero.delete()
    return redirect('m_generos_view')

@login_required
def d_canciones_view(request, cancion_id):
    cancion = get_object_or_404(Canciones, id= cancion_id)
    cancion.delete()
    return redirect('m_canciones_view')
    
@login_required
def d_artistas_view(request, artista_id):
    artista = get_object_or_404(Artistas, id= artista_id)
    artista.delete()
    return redirect('m_artistas_view')

@login_required
def d_albumes_view(request, album_id):
    album = get_object_or_404(Albumes, id= album_id)
    album.delete()
    return redirect('m_albumes_view')

@login_required
def change_genero_view(request, genero_id):
    gene, created = Generos.objects.get_or_create(
        id=genero_id,
    )
    print("---------------------------------", request.user.id)
    if request.method == 'POST':
        form = GenerosForm(request.POST, request.FILES, instance=gene)
        if form.is_valid():
            print("el formulario es valido")
            if form.has_changed():
                new_gene = form.save(commit=False)
                new_gene.pk = genero_id
                new_gene.save()
                messages.success(request, 'Listo, genero actualizado')
            else:
                print("no hizo cambios")
                messages.info(request, 'No has hecho cambios')
        else:
            print("no es valido")
            messages.error(request, 'No se pudo actualizar tu genero')
            
    form = GenerosForm(instance=gene)
    return render(request, 'editar_generos.html', {'form':form, 'gene':gene})

@login_required
def change_artista_view(request, artista_id):
    artis, created = Artistas.objects.get_or_create(
        id=artista_id,
    )
    if request.method == 'POST':
        form = ArtistaForm(request.POST, request.FILES, instance=artis)
        if form.is_valid():
            print("el formulario es valido")
            if form.has_changed():
                new_art = form.save(commit=False)
                new_art.pk = artista_id
                new_art.save()
                messages.success(request, 'Listo, genero actualizado')
            else:
                print("no hizo cambios")
                messages.info(request, 'No has hecho cambios')
        else:
            print("no es valido")
            messages.error(request, 'No se pudo actualizar tu genero')
    form = ArtistaForm(instance=artis)
    return render(request, 'editar_artistas.html', {'form':form, 'artis':artis})

@login_required
def change_album_view(request, album_id):
    albu, created = Albumes.objects.get_or_create(
        id=album_id,
    )
    if request.method == 'POST':
        form = AlbumesForm(request.POST, request.FILES, instance=albu)
        if form.is_valid():
            print("el formulario es valido")
            if form.has_changed():
                new_gene = form.save(commit=False)
                new_gene.pk =  album_id
                new_gene.save()
                messages.success(request, 'Listo, genero actualizado')
            else:
                print("no hizo cambios")
                messages.info(request, 'No has hecho cambios')
        else:
            print("no es valido")
            messages.error(request, 'No se pudo actualizar tu genero')
    form = AlbumesForm(instance=albu)
    return render(request, 'editar_albumes.html', {'form':form, 'albu':albu})

@login_required
def change_cancion_view(request, cancion_id):
    canci, created = Canciones.objects.get_or_create(
        id=cancion_id,
    )
    
    if request.method == 'POST':
        form = CancionesForm(request.POST, request.FILES, instance=canci)
        if form.is_valid():
            print("el formulario es valido")
            if form.has_changed():
                new_gene = form.save(commit=False)
                new_gene.pk = cancion_id
                new_gene.save()
                messages.success(request, 'Listo, genero actualizado')
            else:
                print("no hizo cambios")
                messages.info(request, 'No has hecho cambios')
        else:
            print("no es valido")
            messages.error(request, 'No se pudo actualizar tu genero')
    form = CancionesForm(instance=canci)
    return render(request, 'editar_canciones.html', {'form':form, 'canci':canci})



# Modificar el html al correspondiente

@login_required
def artistas_view(request):
    artistas = Artistas.objects.all()
    return render(request, 'artistas.html', {'artistas':artistas})

@login_required
def canciones_view(request):
    canciones = Canciones.objects.all()
    return render(request, 'canciones.html', {'canciones':canciones})

@login_required
def generos_view(request):
    generos = Generos.objects.all()
    return render(request, 'generos.html', {'generos':generos})

@login_required
def busqueda_view(request):
    artista=None
    album=None
    cancion=None
    if request.method == 'POST':
        print(request.POST['search'])
        artista = Artistas.objects.filter(artista=request.POST['search']).first()
        print(artista)
        album = Albumes.objects.filter(album=request.POST['search']).first()
        print(album)
        cancion = Canciones.objects.filter(cancion=request.POST['search']).first()
        print(cancion)
    return render(request, 'busqueda.html', {'artista':artista, 'album':album, 'cancion':cancion})

@login_required
def bal_canciones_view(request, id_album):
    canciones = Canciones.objects.filter(fk_album=id_album)
    return render(request, 'canciones.html', {'canciones':canciones})

@login_required
def bgen_canciones_view(request, id_genero):
    canciones = Canciones.objects.filter(fk_genero=id_genero)
    return render(request, 'canciones.html', {'canciones':canciones})

@login_required
def bar_albumes_view(request, id_artista):
    albumes = Albumes.objects.filter(fk_artista=id_artista)
    return render(request, 'albumes.html', {'albumes':albumes})
