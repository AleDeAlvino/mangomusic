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
from .models import User
from .forms import ProfileForm, UserForm

# Create your views here.
def Bienvenida_view(request):
    return render(request, 'Bienvenida.html')

def login_view(request):
    if request.method == 'POST':
        print("primer if")
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        print(request.POST['username'])
        print(request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('home_view')
        else:
            print("primer else")
            return render(request, 'Login.html', {'form':AuthenticationForm()})
    else:
        print("segundo else")
        form = AuthenticationForm()
    return render(request, 'Login.html', {'form':form})

def sign_in_view(request):
    print("dentro fun")
    if request.method == 'POST':
        print("primer if")
        form = ProfileForm(request.POST)
        if form.is_valid():
            print("Es valido")
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], last_name=request.POST['last_name'], first_name=request.POST['first_name'], pais=request.POST['pais'], fecha_nac=request.POST['fecha_nac'])
            user.save()
            messages.success(request, 'Listo')
            return redirect('login_view')
        else:
            messages.error(request, 'No se pudo registrar, revisa tus datos')
            print("No Es valido")
    form = ProfileForm()
    return render(request, 'Registro.html', {'form':form})

@login_required
def home_view(request):
    return render(request, 'albumes.html')

@login_required
def change_perfil_view(request):
    return render(request, 'change_perfil.html')

