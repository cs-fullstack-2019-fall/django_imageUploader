from django.db import models


# Create your models here.
class testModel(models.Model):
    name = models.CharField(max_length=100)
    imageFile = models.ImageField(upload_to='DMVApp/')
