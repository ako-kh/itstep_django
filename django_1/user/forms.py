from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

class ProfileUpdateForm(UserChangeForm):
    birth_date = forms.DateField(widget=forms.SelectDateWidget)
    phone_number = PhoneNumberField(region='GE')
    address = forms.CharField(max_length=200, required=False)

    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance.pk:
            self.fields['birth_date'].initial = self.instance.profile.birth_date
            self.fields['phone_number'].initial = self.instance.profile.phone_number
            self.fields['address'].initial = self.instance.profile.address

    def save(self, commit = True):
        user = super().save(commit=commit)

        if commit:
            profile = user.profile
            profile.birth_date = self.cleaned_data['birth_date']
            profile.phone_number = self.cleaned_data['phone_number']
            profile.address = self.cleaned_data['address']
            profile.save()

        return user
