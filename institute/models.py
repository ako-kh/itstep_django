from django.db import models


class Professors(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()
    pass

class Curses(models.Model):
    subject = models.CharField(max_length=30)
    star_date = models.DateField()
    end_date = models.DateField()
    professor = models.ForeignKey(Professors, on_delete=models.SET_NULL, null=True)

class Students(models.Model):
    full_name = models.CharField(max_length=30)
    age = models.IntegerField()
    curse = models.ForeignKey(Curses, on_delete=models.SET_NULL, null=True)
