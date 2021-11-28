from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    country_code = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    contact_picture = models.URLField(null=True)
    is_favourite = models.BooleanField(default = True)
    