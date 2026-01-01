from django.shortcuts import render
from .models import Products
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product_success.html')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

def product_detail(request, product_id):
    product = Products.objects.get(product_id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def edit_product(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return render(request, 'product_success.html')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

def delete_product(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return render(request, 'product_success.html')
    return render(request, 'delete_product.html', {'product': product})

def home(request):
    return render(request, 'home.html')







