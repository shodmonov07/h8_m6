from django.shortcuts import render, get_object_or_404, redirect

from online_shop.forms import ProductForm
from online_shop.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'online_shop/home.html', {'products': products})


def product_detail(request, product_id):
    products = Product.objects.get(id=product_id)
    return render(request, 'online_shop/detail.html', {'products': products})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'online_shop/product_form.html', {'form': form})


def update_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    return render(request, 'online_shop/product_form.html', {'form': form})


def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request, 'online_shop/product_confirm_delete.html', {'product': product})


def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'online_shop/product_add.html', {'form': form})