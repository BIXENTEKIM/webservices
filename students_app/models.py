from django.db import models

class Students(models.Model):
    admno =models.CharField(max_length=20,null=False,blank=False,unique=True)
    name =models.CharField(max_length=50,null=True,blank=True,unique=True)
    age=models.IntegerField()

