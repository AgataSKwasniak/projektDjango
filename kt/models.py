from django.db import models

# Create your models here.
class Kontakt(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=150)
    telefon = models.IntegerField()