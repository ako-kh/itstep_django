from .models import Product
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Product)
def log_product_update(sender, instance: Product, created, **kwargs):
    if not created:
        print(f'Product "{instance.title}" was updated')