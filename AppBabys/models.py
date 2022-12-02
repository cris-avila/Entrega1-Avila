from django.db import models

# Create your models here.

class Bodys(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    talle=models.CharField(max_length=30)
    precio=models.IntegerField()


class Pantalones(models.Model):
    marca= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    talle=models.CharField(max_length=30)
    precio=models.IntegerField()
        

class Remeras(models.Model):
    marca= models.CharField(max_length=30)
    modelo= models.CharField(max_length=30)
    color= models.CharField(max_length=30)
    talle= models.CharField(max_length=30)
    precio=models.IntegerField()



