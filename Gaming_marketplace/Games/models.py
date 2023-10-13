from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    creator = models.CharField(max_length=25)
    genre = models.CharField(max_length=25)
    year = models.DateField()

    