from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.http import HttpResponse
from django.views import View
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
#from portafoliopersonal import utils
from portafoliopersonal.models import Login
from portafoliopersonal.forms import LoginForm

#Este es la pagina del login principal
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/signin')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def home(request): 
    return render(request, 'home.html')


# SI EL USUARIO SE LOGO CORRECTAMENTE  SE REDIRIGE A /PROFILE
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/profile') #profile
        else:
            msg = 'Usuario o contraseña incorrecta'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


# MUESTRA MENSAJE DE BIENVENIDA AL USUARIO
#@login_required -> si para entrar sera requerido iniciar sesion 
def profile(request): 
    return render(request, 'index.html') #profile


# SI EL USUARIO CIERRA SESION MANDA AL LOGIN
def signout(request):
    logout(request)
    return redirect('/signin')    

#requerido
@login_required
class PortafolioP(ListView):
    model = Login
    template_name = 'index.html'

    





class LoginView(ListView):
    model = Login
    template_name = 'login.html'


class Prueba(ListView):
    model = Login
    template_name = 'prueba.html'


class LoginFormInsert(View):
    def get(self, request):
        Frmlogin = LoginForm()

        context = {'form': Frmlogin} 

        return render (request,'login.html', context)

    def post(self, request):
        formulario = LoginForm(request.POST)
        if formulario.is_valid():
            request.session['name_insert'] = formulario.cleaned_data['name']
            request.session['password_insert'] = formulario.cleaned_data['password']
            nameI = request.session['name_insert']
            passwordI = request.session['password_insert']

            return HttpResponse(f'El usuario es: {nameI} y la contraseña es: {passwordI}')
        return HttpResponse('Valores del formulario invalidos')