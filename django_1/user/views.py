from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
)
from django.contrib.auth.views import LoginView
from .forms import ProfileCreationForm
from .models import ProfileModel


class SigneUpView(CreateView):
    model = User
    form_class = ProfileCreationForm
    template_name = 'signe_up.html'
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        form_data = form.cleaned_data
        profile = ProfileModel(
            user = user,
            phone_number=form_data.get('phone_number'),
            address=form_data.get('address'),
            birth_date=form_data.get('birth_date')
        )
        profile.save()
        return super().form_valid(form)

class SigneInView(LoginView):
    template_name = 'signe_in.html'
    next_page = '/'