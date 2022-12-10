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
from portafoliopersonal.models import Login, Portafolio
from portafoliopersonal.forms import LoginForm, PortafioForm

# REGISTRO DE USUARIO
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
            return redirect('/home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

# MENSAJE DE USUARIO CREADO CON EXITO
def home(request): 
    return render(request, 'home.html')


# INICIO DE SESION LOGIN
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            form = PortafioForm()

            return redirect('/profile') #profile
            
        else:
            msg = 'Usuario o contraseña incorrecta'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


# MUESTRA MENSAJE DE BIENVENIDA AL USUARIO
# llamando la tabla de portafolio (portafolio.portafoliopersonal_portafolio)
def profile(request): 
    portafolioall = Portafolio.objects.all()
    return render(request, 'index.html',{'posts': portafolioall}) #profile


# BOTON PARA REGRESAR AL LOGIN DE LA PAGINA home.html
def signout(request):
    logout(request)
    return redirect('/home')    


# SI EL USUARIO CIERRA SESION MANDA AL LOGIN index.html
def signoutx(request):
    logout(request)
    return redirect('/')    







#Creacion de formulario proyecto

class formPortafolio(View):
    template_getall= 'index.html'
    template_get = 'formPortafolio.html'
    #template_get2 = 'index.html'
    context = {}


    #funcion para mostrar los portafolios en index
    def get_portafolios(self,request):
        formx = PortafioForm()
        self.context['formx'] = formx
        self.context['detailx']  = Portafolio.objects.all()
        
        return render(request,self.template_getall,self.context)
    # aun no funcionando


    def get(self,request):
        form = PortafioForm()
        self.context['form'] = form
        self.context['detail'] = Portafolio.objects.all()
        #self.context['detail'] = Profesor.objects.filter(pk=id).first()

        return render(request,self.template_get,self.context)
        #return render(request,self.template_portafolioall,self.context) #self.context
        #formulario = ProfesorForm()
        #context = {'form': formulario}

        #return render(request, self.template_get, context)
    
    def post(self, request):
        form = PortafioForm(request.POST)
        if form.is_valid():
            form.save()

        #self.context['form'] = form
        self.context['detail'] = Portafolio.objects.all()

        #return redirect(request, '/signin', self.context)
        return render(request, 'index.html', self.context)

   

    """def render_posts(request):
        portafolioall = Portafolio.objects.all()

        return render(request, 'index.html', {'posts': portafolioall})"""

        

# Funcion si el usuario quiere crear un portafolio debe iniciar sesion
def requiredloginxportafolio(request): 
    return render(request, 'requiredportafolio.html')



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