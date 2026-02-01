from django.urls import path
from .views import index, on_sale, category

app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('on_sale/', on_sale, name='on_sale'),
    path('category/<str:category_title>/', category, name='category'),
]