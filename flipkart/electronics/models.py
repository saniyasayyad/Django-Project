from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=500)
    price = models.IntegerField()
    description = models.TextField()

    def __str__(self):  # Fix indentation here
        return self.name
