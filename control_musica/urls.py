from django.urls import path
from .import views

urlpatterns = [
    path('artistas/', views.artistas_view, name="artistas_view"),
]