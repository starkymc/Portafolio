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