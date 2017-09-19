from django.db import models
from django_resized import ResizedImageField
from django.core.urlresolvers import reverse

# Create your models here.


class Instructor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)


class Sexo(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.genero

class Tipo(models.Model):
    tipo =  models.CharField(max_length=50)

    def __str__(self):
        return self.tipo

class Rutina (models.Model):
    nombre = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor')
    sexo = models.ForeignKey('Sexo')
    tipo = models.ForeignKey('Tipo')
    descripcion = models.TextField()
    rutina = models.FileField(upload_to='files/pdf')

    def __str__(self):
        return self.nombre

