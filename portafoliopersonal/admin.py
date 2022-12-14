from django.contrib import admin
from .models import Portafolio, IpAddress

# Register your models here.
class PortafolioAdmin(admin.ModelAdmin):
    admin.site.register(Portafolio)
    admin.site.register (IpAddress)
