
from distutils.command.upload import upload
import email
from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria (models.Model):
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f'Categoria {self.id}:{self.descripcion}'

class Comentario (models.Model):
    Nombre = models.CharField(max_length=255)
    Comentario = models.CharField(max_length=255)
    mail = models.EmailField

class post(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=5000)
    imagen = models.ImageField(upload_to='photos')
    
    def __str__(self):
        return self.titulo

