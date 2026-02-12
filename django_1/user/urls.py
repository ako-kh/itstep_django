from django.urls import path
from .views import SigneUpView

app_name = 'user'

urlpatterns = [
    path('signe_up/', SigneUpView.as_view(), name='signe_up')
]