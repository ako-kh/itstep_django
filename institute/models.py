from django.db import models


class Professor(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __str__(self):
        return self.full_name

class Curse(models.Model):
    subject = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.subject

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()
    curse = models.ManyToManyField(Curse)

    def __str__(self):
        return self.full_name
