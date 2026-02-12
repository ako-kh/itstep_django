from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
# from .models import ProfileModel


class ProfileCreationForm(UserCreationForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget)
    phone_number = PhoneNumberField(region='GE')
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']