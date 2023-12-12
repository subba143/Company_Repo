from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key="email")
    company = models.CharField(max_length=150)
    from_date = models.DateField()
    qualification = models.CharField(max_length=70)
    age = models.IntegerField()
    gender = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    address = models.TextField(max_length=250)
    def __str__(self):
        return self.email






