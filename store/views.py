from django.shortcuts import render

from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html')

def equipment(request):
    return render(request, 'store/equipment.html')

def lessons(request):
    return render(request, 'store/lessons.html')

def products(request):
    return render(request, 'store/products.html')

def quality(request):
    return render(request, 'store/quality.html')

