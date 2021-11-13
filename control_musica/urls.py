from django.urls import path
from .import views

urlpatterns = [
    path('configuracion/', views.configuracion_view, name="configuracion_view"),
    path('CRUD/<int:model_id>', views.crud_view, name="crud_view"),
    path('artistas/', views.artistas_view, name="artistas_view"),
    path('add_canciones/', views.add_canciones_view, name="add_canciones_view"),
    path('add_artistas/', views.add_artistas_view, name="add_artistas_view"),
    path('add_albumes/', views.add_albumes_view, name="add_albumes_view"),
    path('add_generos/', views.add_generos_view, name="add_generos_view"),
]