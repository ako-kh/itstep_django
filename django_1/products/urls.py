from django.urls import path
from .views import (
    IndexView,
    on_sale_view,
    category_view,
    ProductDetailView,
    AddProductView,
    ProductUpdateView,
    ProductDeleteView,
    ProductShopView,
    add_remove_wishlist,
    # AddToWishlist,
)

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('on_sale/', on_sale_view, name='on_sale'),
    path('category/<str:category_title>/', category_view, name='category'),
    path('details/<int:product_pk>/', ProductDetailView.as_view(), name='details'),
    path('add_product', AddProductView.as_view(), name='add_product'),
    path('update_product/<int:product_pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete_product/<int:product_pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('shop/', ProductShopView.as_view(), name='shop_product'),
    path('add_remove_wishlist/<int:product_pk>/', add_remove_wishlist, name='add_remove_wishlist'),
]