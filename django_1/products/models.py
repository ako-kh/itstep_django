from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.contrib.auth.models import User
from decimal import Decimal

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        related_name='products'
    )
    sale = models.IntegerField(
        null=True,
        blank=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ]
    )
    on_sale = models.BooleanField(default=False)

    main_image = models.ImageField(upload_to='product_images', default='default.jpg', blank=True)
    image1 = models.ImageField(upload_to='product_images', null=True, blank=True)
    image2 = models.ImageField(upload_to='product_images', null=True, blank=True)
    image3 = models.ImageField(upload_to='product_images', null=True, blank=True)
    image4 = models.ImageField(upload_to='product_images', null=True, blank=True)

    wishlist = models.ManyToManyField(User, related_name='wishlist')

    cart = models.ManyToManyField(User, related_name='cart')

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'

    @property
    def new(self):
        days_old =  (timezone.now() - self.created_at).days

        if 10 < days_old:
            return True
        else:
            return False

    @property
    def sale_price(self):
        if self.on_sale:
            sale_price = self.price * (1 - Decimal(self.sale) / 100)
            sale_price = round(sale_price, 2)
            return sale_price

        return self.price

    def __str__(self):
        return f"{self.category} -- {self.title}"
