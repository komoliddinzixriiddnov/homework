from django.db import models

class Teacher(models.Model):
    name =models.CharField(max_length=20)
    specialites =models.CharField(max_length=20)
    teachers = models.CharField(max_length=20)

class Subject(models.Model):
    name = models.CharField(max_length=20)
    specialites = models.CharField(max_length=20)
    teachers = models.CharField(max_length=20)
