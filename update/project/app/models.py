from unicodedata import name
from django.db import models

# Create your models here.

class employee(models.Model):

    name1=models.TextField(max_length=10)
    name2=models.TextField(max_length=10)