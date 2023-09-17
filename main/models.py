from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    tier = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
    
    