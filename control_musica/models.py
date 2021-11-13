from django.db import models

# Create your models here.
class Generos(models.Model):
    genero = models.CharField(max_length = 50)

class Artistas(models.Model):
    artista = models.CharField(max_length = 50)
    seguidores = models.IntegerField(default=0)
    verificacion = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='artistas/', default='albumes/default.jpg')

class Albumes(models.Model):
    fk_artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    album = models.CharField(max_length = 50)
    fecha = models.DateField()
    foto = models.ImageField(upload_to='albumes/', default='albumes/default.jpg')

class Canciones(models.Model):
    fk_album = models.ForeignKey(Albumes, on_delete=models.CASCADE)
    fk_genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    cancion = models.CharField(max_length = 50)
    reproducciones = models.IntegerField(default=0)
    duracion = models.IntegerField()