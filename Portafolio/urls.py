from django.contrib import admin
from django.urls import path
from portafoliopersonal import views
from django.contrib.auth.decorators import login_required
from portafoliopersonal.views import (
home, signup, signin,signout,profile,signoutx, requiredloginxportafolio,
generate_preview,crear,profile_sinuser)

#signoutx

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('portafolio/', PortafolioP, name='index'),


    #path('signin/portafolio/',PortafolioP, name='signin'),



    path('home/', home, name='home'),
    path('signup/',signup, name='signup'),

    #working
    #path('signin/',signin, name='signin'),
    path('',signin, name='signin'),
    path('signout/',signout, name='signout'),
    path('profile/',login_required(profile,login_url='/profile_sinuser/'), name='profile'),

    #path('crearportafolio/',login_required(formPortafolio.as_view(),login_url='/requiredxportf/'), name='crear'),
    #path('crearportafolio/',formPortafolio.as_view(), name='crear'),

    path('signoutx/',signoutx, name='signoutx'),
    path('requiredxportf/',requiredloginxportafolio, name='loginrequiredpf'),
    
    path('profile_sinuser/',profile_sinuser, name='profile_sinuser'),


    # preview-link
    #path('urlpreview/', urlpreview, name='generate_preview'),
    path('generate_preview/', generate_preview, name='generate'),
    ###
    path('crear/', login_required(views.crear,login_url='/requiredxportf/'), name='create'),
    
]



