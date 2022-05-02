import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Mensaje(models.Model):
    fecha = models.DateField('date published')
    lugar = models.CharField(max_length=200)
    usuario =  models.CharField(max_length=200)
    red_social = models.CharField(max_length=200)
   