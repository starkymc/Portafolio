from django.db import models
from django.contrib.auth.models import User



class Portafolio(models.Model):
    foto = models.CharField(max_length=400)
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    tags = models.CharField(max_length=100)
    github = models.CharField(max_length=450)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.project_name + ' - by ' + self.user.username
    #+ self.user.username

    def to_json(self):
       model_in_jason  = {
            'foto': self.foto,
            'project_name':  self.project_name,
            'description': self.description,
            'tags': self.tags,
            'github': self.github
       }
       return model_in_jason   

class IpAddress (models.Model):
    pub_date=models.DateField("Fecha de petición")
    ip_address = models.GenericIPAddressField()

    class Meta:
        verbose_name = 'Direccion IP'
        verbose_name_plural = 'Direcciones de Ip'
    def __str__(self):
        return f"{self.ip_address}" 
   

   

   
