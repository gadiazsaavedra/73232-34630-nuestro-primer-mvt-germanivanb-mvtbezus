from django.db import models


# Create your models here.

class Familiares(models.Model):

    nombre = models.CharField(max_length=50)
    fecha = models.CharField(max_length=50)
    agno = models.CharField(max_length=50)
