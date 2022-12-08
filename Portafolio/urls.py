from django.contrib import admin
from django.urls import path

from portafoliopersonal.views import ( PortafolioP,Prueba,LoginView,
home, signup, signin,signout,profile )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('portafolio/', PortafolioP, name='index'),


    #path('signin/portafolio/',PortafolioP, name='signin'),

    path('prueba/', Prueba.as_view(), name='prueba'),
    #path('login/', LoginView.as_view(), name='login'),


    path('home/', home, name='home'),
    path('signup/',signup, name='signup'),

    path('signin/',signin, name='signin'),
    path('signout/',signout, name='signout'),
    path('profile/',profile, name='profile'),

]
