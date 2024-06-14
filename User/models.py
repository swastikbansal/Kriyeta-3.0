from django.db import models
from datetime import datetime

# Create your models here.
class UserModel(models.Model) :
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    country = models.CharField(max_length = 100)
    date = models.DateField()

    def __str__(self):
        return self.username