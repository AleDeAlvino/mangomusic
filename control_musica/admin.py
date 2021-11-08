from django.contrib import admin
from .models import Generos, Artistas, Albumes, Canciones

# Register your models here.
admin.site.register(Generos)
admin.site.register(Artistas)
admin.site.register(Albumes)
admin.site.register(Canciones)