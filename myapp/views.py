from django.shortcuts import render,redirect
from .models import Products
from .forms import ProductForm

# Create your views here.
def product_list_view(request):
    products = Products.objects.all()
    return render(request, 'product_list.html', {'products': products})

def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(request, 'product_list.html')
    return redirect(request, 'product_form.html', {'form': form})

def product_update_view(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(request, 'product_list.html')
    return render(request, 'product_form.html', {'form': form, 'product': product})

def product_delete_view(request, product_id):
    product = Products.objects.get(product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect(request, 'product_list.html')
    return render(request, 'product_confirm_delete.html', {'product': product})

def home(request):
    return render(request, 'home.html')










