from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.TextField()
    password = models.TextField()


    def __str__(self):
        return self.name

    def to_json(self):
        login_in_json = {
            'name': self.name,
            'password': self.password
        }

        return login_in_json

class Portafolio(models.Model):
    foto = models.CharField(max_length=400)
    project_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    tags = models.CharField(max_length=100)
    github = models.CharField(max_length=450)

    def to_json(self):
       model_in_jason  = {
            'foto': self.foto,
            'project_name':  self.project_name,
            'description': self.description,
            'tags': self.tags,
            'github': self.github
       }
       return model_in_jason   


   
