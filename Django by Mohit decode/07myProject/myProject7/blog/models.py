from django.db import models

# Create your models here.
from django.db import models

class Form(models.Model):
    username = models.CharField(max_length=100)
    password = models.IntegerField()