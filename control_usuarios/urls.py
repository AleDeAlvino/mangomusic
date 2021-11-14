from django.urls import path
from .import views

urlpatterns = [
    path('', views.Bienvenida_view, name="Bienvenida_view"),
    path('login/', views.login_view, name="login_view"),
    path('sign_in/', views.sign_in_view, name="sign_in_view"),
    path('change/<int:user_id>/', views.change_perfil_view, name="change_perfil_view"),
    path('home/', views.home_view, name="home_view"),
    path('change_password_view/', views.change_password_view, name="change_password_view"),
    path('AboutUs/', views.aboutUs_view, name="about_us_view"),
    path('Premium/', views.premium_view, name="premium_view"),
    path('Soporte/', views.soporte_view, name="soporte_view"),
    path('logout/', views.logout_view, name="logout_view"),
]