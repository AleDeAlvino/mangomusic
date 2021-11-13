from django.urls import path
from .import views

urlpatterns = [
    path('configuracion/', views.configuracion_view, name="configuracion_view"),
    path('CRUD/<int:model_id>', views.crud_view, name="crud_view"),
    path('artistas/', views.artistas_view, name="artistas_view"),
]