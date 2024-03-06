from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

class Book(models.Model):
    title = models.CharField(max_length=20, validators=[MaxValueValidator(25)])

    description = models.TextField()
    price = models.FloatField()
    caunt =models.IntegerField()

    def __str__(self):
        return f"{self.title}"


class Student(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    group_number = models.CharField(max_length=20)
    usern = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Bookingbook(models.Model):
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    talked_data = models.DateTimeField()
    returned = models.DateTimeField(null=True)


