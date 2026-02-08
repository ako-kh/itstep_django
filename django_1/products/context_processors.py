from .models import Category, Product
from django.db.models import Count

def global_context(request):
    categories = Category.objects.filter(products__isnull=False).distinct()
    categories = categories.annotate(product_count=Count('products'))
    last_five_products = Product.objects.all().order_by('-created_at')[:5]

    context = {
        'categories': categories,
        'last_five_products': last_five_products
    }

    return context