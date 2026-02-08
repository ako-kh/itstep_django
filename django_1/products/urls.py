from django.urls import path
from .views import (
    index_view,
    on_sale_view,
    category_view,
    details_view,
    add_product_view,
    update_product_view,
    delete_product_view,
)

app_name = 'products'

urlpatterns = [
    path('', index_view, name='index'),
    path('on_sale/', on_sale_view, name='on_sale'),
    path('category/<str:category_title>/', category_view, name='category'),
    path('details/<int:product_pk>/', details_view, name='details'),
    path('add_product', add_product_view, name='add_product'),
    path('update_product/<int:product_pk>/', update_product_view, name='update_product'),
    path('delete_product/<int:product_pk>/', delete_product_view, name='delete_product'),
]