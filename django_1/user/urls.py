from django.urls import path
from .views import SigneUpView, SigneInView

app_name = 'user'

urlpatterns = [
    path('signe_up/', SigneUpView.as_view(), name='signe_up'),
    path('signe_in/', SigneInView.as_view(), name='signe_in'),
]