from django.db import models
from django.conf import settings

class Contact(models.Model):
    f_name=models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    contact_nu=models.SmallIntegerField()
    email=models.EmailField()

# Create your models here.
