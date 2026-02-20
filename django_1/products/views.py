from django.contrib.auth.decorators import login_required
from django.db.models import F, ExpressionWrapper, DecimalField
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Category, Product
from .forms import AddProductForm, UpdateProductForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# def index_view(request):
#     products = Product.objects.filter(is_available=True).order_by('price').select_related('category')
#     products = products.annotate(
#         sale_price=ExpressionWrapper(
#             F("price") * (1 - F("sale") / 100.0),
#             output_field=DecimalField(max_digits=10, decimal_places=2),
#         )
#     )
#     # products = products.annotate() todo add new bool
#     context = {
#         'products': products,
#     }
#     return render(request, 'index.html', context)


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'products'

    def get_queryset(self):
        products = Product.objects.filter(is_available=True).order_by('price').select_related('category')
        products = products.annotate(
            sale_price=ExpressionWrapper(
                F("price") * (1 - F("sale") / 100.0),
                output_field=DecimalField(max_digits=10, decimal_places=2),
            )
        )

        return products


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


# def details_view(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#     sale_price = None
#     if product.on_sale:
#         sale_price = float(product.price) * (1 - product.sale / 100)
#
#     context = {
#         'product': product,
#         'sale_price': sale_price,
#     }
#
#     return render(request, 'details.html', context)


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'
    template_name = 'details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        product = context.get('product')
        sale_price = None
        if product.on_sale:
            sale_price = float(product.price) * (1 - product.sale / 100)

        context['sale_price'] = sale_price

        return context


# def add_product_view(request):
#     if request.method == 'POST':
#         form = AddProductForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return redirect('products:index')
#
#     else:
#         form = AddProductForm()
#
#     return render(request, 'add_product.html', {'form': form})


class AddProductView(CreateView):
    model = Product
    form_class = AddProductForm
    template_name = 'add_product.html'
    success_url = '/'


# def update_product_view(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#
#     if request.method == 'POST':
#         form = UpdateProductForm(request.POST, instance=product)
#
#         if form.is_valid():
#             form.save()
#             return redirect('products:index')
#
#     else:
#         form = UpdateProductForm(instance=product)
#
#     return render(request, 'update_product.html', {'form': form})


class ProductUpdateView(UpdateView):
    model = Product
    pk_url_kwarg = 'product_pk'
    queryset = Product.objects.filter(is_available=True)
    form_class = UpdateProductForm
    template_name = 'update_product.html'

    def get_success_url(self):
        return reverse_lazy('products:details', kwargs={'product_pk': self.object.pk})


# def delete_product_view(request, product_pk):
#     product = get_object_or_404(Product, pk=product_pk)
#
#     if request.method == 'POST':
#         product.delete()
#         return redirect('products:index')
#
#     return redirect('products:details', product_pk=product_pk)


class ProductDeleteView(DeleteView):
    model = Product
    pk_url_kwarg = 'product_pk'
    queryset = Product.objects.filter(is_available=True)
    success_url = '/'


class ProductShopView(ListView):
    model = Product
    template_name = 'shop.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_queryset(self):
        products = Product.objects.filter(is_available=True).order_by('price').select_related('category')
        products = products.annotate(
            sale_price=ExpressionWrapper(
                F("price") * (1 - F("sale") / 100.0),
                output_field=DecimalField(max_digits=10, decimal_places=2),
            )
        )

        return products


# class AddToWishlist(BaseUpdateView):
#     model = Product
#     pk_url_kwarg = 'product_pk'
#     fields = ['wishlist']
#     success_url = reverse_lazy('products:index')
#
#     def form_valid(self, form):
#         product = form.save(commit=False)
#         product.wishlist.add(self.request.user)
#         product.save()
#         return super().form_valid(form)

@login_required
def add_remove_wishlist(request, product_pk):
    product = get_object_or_404(Product, pk=product_pk)
    profile = request.user.profile

    if request.method == 'POST':

        if product not in profile.wishlist.all():
            profile.wishlist.add(product)
        else:
            profile.wishlist.remove(product)

        profile.save()

    return redirect(request.POST.get('next', '/'))

class WishlistView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'wishlist.html'
    context_object_name = 'wishlist_products'

    def get_queryset(self):
        wishlist_products = Product.objects.filter(wishlist=self.request.user.profile).select_related('category')
        wishlist_products = wishlist_products.annotate(
            sale_price=ExpressionWrapper(
                F("price") * (1 - F("sale") / 100.0),
                output_field=DecimalField(max_digits=10, decimal_places=2),
            )
        )
        return wishlist_products

