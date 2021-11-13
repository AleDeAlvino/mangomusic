from django.shortcuts import render
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
# from .models import User
# from .forms import 

# Create your views here.

@login_required
def configuracion_view(request):
    return render(request, 'configuracion.html')

@login_required
def crud_view(request, model_id):
    return render(request, 'CRUD.html', {'model_id':model_id})

@login_required
def artistas_view(request):
    return render(request, 'agregar_artistas.html')