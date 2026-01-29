from django.db.models import Count, F, ExpressionWrapper, DecimalField
from django.shortcuts import render
from products.models import Category, Product


def index(request):
    products = Product.objects.filter(is_available=True).order_by('price')
    categories = Category.objects.filter(products__isnull=False).distinct()
    categories = categories.annotate(product_count=Count('products'))

    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'index.html', context)

def on_sale(request):
    on_sale_products = Product.objects.filter(on_sale=True, is_available=True)

    on_sale_products = on_sale_products.annotate(
        sale_price=ExpressionWrapper(
            F("price") * (1 - F("sale") / 100.0),
            output_field=DecimalField(max_digits=10, decimal_places=2),
        )
    )

    return render(request, 'on_sale.html', {'on_sale_products': on_sale_products})