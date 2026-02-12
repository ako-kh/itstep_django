from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(region='GE')
    address = models.CharField(max_length=200, null=True, blank=True)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - profile'
