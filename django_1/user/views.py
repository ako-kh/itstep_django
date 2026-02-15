from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    UpdateView,
)
from django.contrib.auth.views import LoginView, LogoutView
from .forms import ProfileCreationForm, ProfileUpdateForm
from .models import ProfileModel


class SigneUpView(CreateView):
    model = User
    form_class = ProfileCreationForm
    template_name = 'signe_up.html'
    success_url = reverse_lazy('user:signe_in')

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

class SigneOutView(LogoutView):
    next_page = '/'

class MyAccountView(UpdateView):
    model = User
    form_class = ProfileUpdateForm
    pk_url_kwarg = 'profile_pk'
    template_name = 'my_account.html'

    def get_success_url(self):
        return reverse_lazy('user:my_account', kwargs={'profile_pk': self.object.pk})

    def get_queryset(self):
        return self.model.objects.filter(pk=self.request.user.pk)

    # def form_valid(self, form):
    #     user = form.save(commit=False)
    #
    #     if user.pk == self.request.user.pk:
    #         user.save()
    #         return super().form_valid(form)
    #
    #     return super().form_invalid(form)
