from django.urls import path
from .import views

urlpatterns = [
    path('', views.Bienvenida_view, name="Bienvenida_view"),
    path('login/', views.login_view, name="login_view"),
    path('sign_in/', views.sign_in_view, name="sign_in_view"),
    path('change/', views.change_perfil_view, name="change_perfil_view"),
    path('home/', views.home_view, name="home_view"),
]