from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    Pseudo = models.CharField(max_length=10)
    Password = models.CharField(max_length=30)
    Confirm_password = models.CharField(max_length=30)