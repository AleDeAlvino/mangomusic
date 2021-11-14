from django.urls import path
from .import views

urlpatterns = [
    path('configuracion/', views.configuracion_view, name="configuracion_view"),
    path('CRUD/<int:model_id>', views.crud_view, name="crud_view"),
    path('artistas/', views.artistas_view, name="artistas_view"),
    path('canciones/', views.canciones_view, name="canciones_view"),

    path('add_canciones/', views.add_canciones_view, name="add_canciones_view"),
    path('add_artistas/', views.add_artistas_view, name="add_artistas_view"),
    path('add_albumes/', views.add_albumes_view, name="add_albumes_view"),
    path('add_generos/', views.add_generos_view, name="add_generos_view"),

    path('m_generos/', views.m_generos_view, name="m_generos_view"),
    path('m_artistas/', views.m_artistas_view, name="m_artistas_view"),
    path('m_albumes/', views.m_albumes_view, name="m_albumes_view"),
    path('m_canciones/', views.m_canciones_view, name="m_canciones_view"),

    path('d_generos/<int:genero_id>', views.d_generos_view, name="d_generos_view"),
    path('d_canciones/<int:cancion_id>', views.d_canciones_view, name="d_canciones_view"),
    path('d_artistas/<int:artista_id>', views.d_artistas_view, name="d_artistas_view"),
    path('d_albumes/<int:album_id>', views.d_albumes_view, name="d_albumes_view"),

    path('change_genero/<int:genero_id>', views.change_genero_view, name="change_genero_view"),
    path('change_artista/<int:artista_id>', views.change_artista_view, name="change_artista_view"),
    path('change_album/<int:album_id>', views.change_album_view, name="change_album_view"),
    path('change_cancion/<int:cancion_id>', views.change_cancion_view, name="change_cancion_view"),
    
    path('busqueda/', views.busqueda_view, name="busqueda_view"),
]