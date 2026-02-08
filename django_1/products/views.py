from django.db.models import F, ExpressionWrapper, DecimalField
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Category, Product
from .forms import AddProductForm, UpdateProductForm


def index_view(request):
    products = Product.objects.filter(is_available=True).order_by('price').select_related('category')
    products = products.annotate(
        sale_price=ExpressionWrapper(
            F("price") * (1 - F("sale") / 100.0),
            output_field=DecimalField(max_digits=10, decimal_places=2),
        )
    )
    # products = products.annotate() todo add new bool
    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def on_sale_view(request):
    on_sale_products = Product.objects.filter(on_sale=True, is_available=True)

    on_sale_products = on_sale_products.annotate(
        sale_price=ExpressionWrapper(
            F("price") * (1 - F("sale") / 100.0),
            output_field=DecimalField(max_digits=10, decimal_places=2),
        )
    )

    return render(request, 'on_sale.html', {'on_sale_products': on_sale_products})


def category_view(request, category_title):
    category = get_object_or_404(Category, title=category_title)

    products = Product.objects.filter(
        is_available=True,
        category=category
    ).order_by('price')

    product_count = products.count()

    context = {
        'products': products,
        'category': category,
        'product_count': product_count,
    }

    return render(request, 'category.html', context)


def details_view(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    return render(request, 'details.html', {'product': product})


def add_product_view(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('products:index')

    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})


def update_product_view(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)

    if request.method == 'POST':
        form = UpdateProductForm(request.POST, instance=product)

        if form.is_valid():
            form.save()
            return redirect('products:index')

    else:
        form = UpdateProductForm(instance=product)

    return render(request, 'update_product.html', {'form': form})
