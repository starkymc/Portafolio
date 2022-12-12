from django.db import IntegrityError
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
from django.contrib.auth.models import User

#link-preview-lib
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
####

from portafoliopersonal.models import  Portafolio
from portafoliopersonal.forms import  PortafioForm

# REGISTRO DE USUARIO
def signup(request):
   
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('profile')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Este usuario ya existe."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Las contraseñas no coinciden."})



# MENSAJE DE USUARIO CREADO CON EXITO
def home(request): 
    return render(request, 'home.html')


# INICIO DE SESION LOGIN
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {"form": AuthenticationForm, "error": "Usuario o contraseña incorrecta."})

        login(request, user)
        return redirect('profile')


# MUESTRA MENSAJE DE BIENVENIDA AL USUARIO
# llamando la tabla de portafolio (portafolio.portafoliopersonal_portafolio)
def profile(request): 

    portafolioall = Portafolio.objects.filter(user=request.user)
    
    return render(request, 'index.html',{'posts': portafolioall}) #profile


# BOTON PARA REGRESAR AL LOGIN DE LA PAGINA home.html
def signout(request):
    logout(request)
    return redirect('/home')    


# SI EL USUARIO CIERRA SESION MANDA AL LOGIN index.html
def signoutx(request):
    logout(request)
    return redirect('/')    

def profile_sinuser(request):
    return render(request,'index.html')


# funcion generar la vista aqui se llaman las 3 funciones creadas
def generate_preview(request):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Max-Age': '3600',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

    url = request.GET.get('link')
    #print(url)
    req = requests.get(url, headers)
    html = BeautifulSoup(req.content, 'html.parser')
    meta_data = {
        'title': get_title(html),
        'description': get_description(html),
        'image': get_image(html),
    }

    print(meta_data)

    return JsonResponse(meta_data)

# funcion para obtener description de  title
def get_title(html):
    """Scrape page title."""
    title = None
    if html.title.string:
        title = html.title.string
    elif html.find("meta", property="og:title"):
        title = html.find("meta", property="og:title").get('content')
    elif html.find("meta", property="twitter:title"):
        title = html.find("meta", property="twitter:title").get('content')
    elif html.find("h1"):
        title = html.find("h1").string
    return title

# funcion para obtener description de  url
def get_description(html):
    """Scrape page description."""
    description = None
    if html.find("meta", property="description"):
        description = html.find("meta", property="description").get('content')
    elif html.find("meta", property="og:description"):
        description = html.find(
            "meta", property="og:description").get('content')
    elif html.find("meta", property="twitter:description"):
        description = html.find(
            "meta", property="twitter:description").get('content')
    elif html.find("p"):
        description = html.find("p").contents
    return description

# funcion para obtener imagen previa de  url
def get_image(html):

    image = None
    if html.find("meta", property="image"):
        image = html.find("meta", property="image").get('content')
    elif html.find("meta", property="og:image"):
        image = html.find("meta", property="og:image").get('content')
    elif html.find("meta", property="twitter:image"):
        image = html.find("meta", property="twitter:image").get('content')
    elif html.find("img", src=True):
        image = html.find_all("img").get('src')
    return image

###############

def crear(request):
    if request.method == "GET":
        return render(request, 'formPortafolio.html', {"form": PortafioForm})
    else:
        try:
            form = PortafioForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('profile')
        except ValueError:
            return render(request, 'formPortafolio.html', {"form": PortafioForm, "error": "Error creating portfolio."})

        

# Funcion si el usuario quiere crear un portafolio debe iniciar sesion
def requiredloginxportafolio(request): 
    return render(request, 'requiredportafolio.html')






