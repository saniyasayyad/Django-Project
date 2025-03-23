from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
# Create your views here.

def home(request):
    return render(request, 'electronics/home.html')

def product_detail(request):
    prod = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
<<<<<<< HEAD
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
=======
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
>>>>>>> aee1c01f7da304bc88bb1521251d8b687b9a59a6
    return render(request, 'electronics/product_detail.html', {"prod":prod, 'form':form})

def delete_product(request, id):
            prod = get_object_or_404(Product, id=id)
            prod.delete()
            return redirect('product_detail')

def update_product(request, id):
        prod = get_object_or_404(Product, id=id)

        if request.method == 'POST':
<<<<<<< HEAD
            form = ProductForm(request.POST, request.FILES, instance=prod)
=======
            form = ProductForm(request.POST, instance=prod)
>>>>>>> aee1c01f7da304bc88bb1521251d8b687b9a59a6
            if form.is_valid():
                form.save()
                return redirect('product_detail')
        else:
            form = ProductForm(instance=prod)

        return render(request, 'electronics/update_product.html',{"form":form, "prod":prod})


       