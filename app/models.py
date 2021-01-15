from django.db import models

# Create your models here.
class Account(models.Model):
    email = models.CharField(max_length=64,unique=True,primary_key=True)
    number = models.CharField(max_length=15,blank=True)
    password = models.CharField(max_length=256, blank=False)
    product_key = models.CharField(max_length=256, default="")
    date_created = models.DateTimeField(auto_now=True)
