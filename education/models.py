from django.db import models

class Teacher(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    speciality = models.CharField(max_length=20)
