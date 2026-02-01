from .models import Category
from django.db.models import Count

def global_context(request):
    categories = Category.objects.filter(products__isnull=False).distinct()
    categories = categories.annotate(product_count=Count('products'))

    context = {
        'categories': categories,
    }

    return context