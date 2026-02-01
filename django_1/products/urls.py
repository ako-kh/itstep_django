from django.urls import path
from .views import (
    index_view,
    on_sale_view,
    category_view,
    details_view,
)

app_name = 'products'

urlpatterns = [
    path('', index_view, name='index'),
    path('on_sale/', on_sale_view, name='on_sale'),
    path('category/<str:category_title>/', category_view, name='category'),
    path('details/<int:product_pk>/', details_view, name='details'),
]