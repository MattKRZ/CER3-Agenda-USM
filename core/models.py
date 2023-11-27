from django.db import models

# Create your models here.

class Evento(models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    tipo = models.CharField(max_length=255)
    segmentos = models.ManyToManyField('Segmento')


class Segmento(models.Model):
    nombre = models.CharField(max_length=255)