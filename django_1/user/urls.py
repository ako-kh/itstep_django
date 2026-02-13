from django.urls import path
from .views import SigneUpView, SigneInView, SigneOutView

app_name = 'user'

urlpatterns = [
    path('signe_up/', SigneUpView.as_view(), name='signe_up'),
    path('signe_in/', SigneInView.as_view(), name='signe_in'),
    path('signe_out/', SigneOutView.as_view(), name='signe_out'),
]