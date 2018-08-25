from django.db import models


# Create your models here.
class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=25)
    is_login = models.BooleanField(default=False)

    def __str__(self):
        return self.email
