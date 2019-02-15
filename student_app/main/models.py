from django.db import models

class Person(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=50)
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=12, null=True, blank=True)
    startday = models.DateField()
    endday = models.DateField()
    group = models.CharField(max_length=10)
    university = models.CharField(max_length=100)

class Document(models.Model):
    TYPE = (
        ('P', 'Passport'),
        ('S', 'Student ID'),
        ('B', 'Birth Certificate')
    )
    number = models.CharField(max_length=9, primary_key=True)
    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    issue_date = models.DateField()
    type = models.CharField(max_length=1, choices=TYPE)
    scan = models.CharField(max_length=50)