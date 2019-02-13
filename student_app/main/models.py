from django.db import models
from django.db.models.fields import CharField

class Person(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=100)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=11)
    startday = models.DateField()
    endday = models.DateField()
    group = models.CharField(max_length=10)
    university = models.CharField(max_length=20)

class Document(models.Model):
    TYPE = (
        ('P', 'Passport'),
        ('S', 'Student ID'),
        ('B', 'Birth Certificate')
    )
    number = models.CharField(max_length=20)
    issue_date = models.DateField()
    type = CharField(max_length=1, choices=TYPE)