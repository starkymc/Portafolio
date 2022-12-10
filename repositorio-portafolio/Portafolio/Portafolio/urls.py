from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required
from portafoliopersonal.views import ( Prueba,LoginView,
home, signup, signin,signout,profile,formPortafolio,login,signoutx, requiredloginxportafolio)

#signoutx

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('portafolio/', PortafolioP, name='index'),


    #path('signin/portafolio/',PortafolioP, name='signin'),

    path('prueba/', Prueba.as_view(), name='prueba'),
    #path('login/', LoginView.as_view(), name='login'),


    path('home/', home, name='home'),
    path('signup/',signup, name='signup'),

    #working
    #path('signin/',signin, name='signin'),
    path('',signin, name='signin'),
    path('signout/',signout, name='signout'),
    path('profile/',profile, name='profile'),

    path('crearportafolio/',login_required(formPortafolio.as_view(),login_url='/requiredxportf/'), name='crear'),
    #path('crearportafolio/',formPortafolio.as_view(), name='crear'),

    path('signoutx/',signoutx, name='signoutx'),
    path('login/',login, name='login'),
    path('requiredxportf/',requiredloginxportafolio, name='loginrequiredpf'),
]

