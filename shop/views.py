from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Category
from .forms import ProductForm, CategoryForm

def products_view(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

def product_add_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect(product.get_absolute_url())
    else:
        form = ProductForm()
    return render(request, 'product_add.html', {'form': form})

def category_add_view(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_view')
    else:
        form = CategoryForm()
    return render(request, 'category_add.html', {'form': form})
