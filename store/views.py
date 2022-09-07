from multiprocessing import context
from django.shortcuts import render, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Category, Product
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator


def home(request):
    return render(request, 'store/home.html')

def all_products(request):
    products = Product.products.all()
    return render(request, 'store/products/products.html', {'products': products})


def dashboard(request):
    return render(request, 'store/dashboard.html')

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html')

def equipment(request):
    return render(request, 'store/equipment.html')

def lessons(request):
    return render(request, 'store/lessons.html')

def products(request,category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})

def quality(request):
    return render(request, 'store/quality.html')

def eggs(request):
    products = Product.objects.all()
    return render(request, 'store/eggs.html',{'products': products})


# Products
class CategoryView(View):
    def get(self, *args, **kwargs):
        context={'i':range(0,16)}
        return render(self.request, 'store/products.html')

#add views
class AddCategory(SuccessMessageMixin,CreateView):
    model = Category
    fields = ('__all__')
    template_name = 'store/add-category.html'
    success_message = "Category was added successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('store:add-category')

class AddProduct(SuccessMessageMixin,CreateView):
    model = Product
    fields = ('__all__')
    template_name = 'store/add-product.html'
    success_message = "Product was added successfully"

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('store:add-product')

#####################################################################################################
def categories(request):
    return {
        'categories': Category.objects.all()
    }

def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category': category, 'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})
