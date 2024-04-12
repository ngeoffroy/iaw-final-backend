from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

"""
@author ngeoffroy 
Creo el modelo base de la aplicación
Utilizo el campo mail para la identificación del usuario
"""
class CustomUser(AbstractUser):
    email = models.CharField(max_length=45, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']