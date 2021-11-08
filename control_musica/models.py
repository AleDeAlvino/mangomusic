from django.db import models

# Create your models here.
class Generos(models.Model):
    genero = models.CharField(max_length = 50)

class Artistas(models.Model):
    artista = models.CharField(max_length = 50)
    seguidores = models.IntegerField()
    verificacion = models.BooleanField(default=False)

class Albumes(models.Model):
    fk_artista = models.ForeignKey(Artistas, on_delete=models.CASCADE)
    album = models.CharField(max_length = 50)
    fecha = models.DateField()

class Canciones(models.Model):
    fk_album = models.ForeignKey(Albumes, on_delete=models.CASCADE)
    fk_genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
    cancion = models.CharField(max_length = 50)
    reproducciones = models.IntegerField()
    duracion = models.IntegerField()