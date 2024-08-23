from django.db import models

# Create your models here.

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    phone = models.CharField(max_length=14)
    city = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
