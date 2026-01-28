from django.db import models


class Professor(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()
    pass

class Curse(models.Model):
    subject = models.CharField(max_length=30)
    star_date = models.DateField()
    end_date = models.DateField()
    professor = models.ForeignKey(Professor, on_delete=models.SET_NULL, null=True)

class Student(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()
    curse = models.ForeignKey(Curse, on_delete=models.SET_NULL, null=True)
