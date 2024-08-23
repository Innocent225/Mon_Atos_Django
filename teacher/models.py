from django.db import models

# Create your models here.

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=14)
    city = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)