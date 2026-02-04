# myproject/myapp/views.py
from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm


def product_list_view(request):
    products = Products.objects.all()
    return render(request, 'InvApp/product_list.html', {'products': products})

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect( 'product-list')
    else:
        form = ProductForm()
    return render(request, 'InvApp/product_form.html', {'form': form})

def product_update_view(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product-list')
    else:        
        form = ProductForm(instance=product)
    return render(request, 'InvApp/product_form.html', {'form': form, 'product': product})

def product_delete_view(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product-list')
    return render(request, 'InvApp/product_confirm_delete.html', {'product': product})

def home(request):
    return render(request, 'InvApp/home.html')










