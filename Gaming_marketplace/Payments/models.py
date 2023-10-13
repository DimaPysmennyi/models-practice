from django.db import models

# Create your models here.
class Payment(models.Model):
    username = models.CharField(max_length=25)
    amount_money = models.IntegerField()
    comment = models.TextField(default="lorem ipsum")