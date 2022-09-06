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

# class AccountView(LoginRequiredMixin,generic.View):
#     login_url = '/user/login'
#     redirect_field_name = 'user/cust-account/'
#     def get(self,*args, **kwargs):
#         return render(self.request, 'store/cust-account.html')

def all_products(request):
    products = Product.products.all()
    return render(request, 'store/products/products.html', {'products': products})


# def dashboard(request):
#     return render(request, 'store/dashboard.html')

def about(request):
    return render(request, 'store/about.html')

def contacts(request):
    return render(request, 'store/contacts.html')

# def equipment(request):
# return render(request, 'store/equipment.html')

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

# Registration
# class SignupView(generic.View):
#     def get(self,*args,**kwargs):
#         context = {
#             'user_creation_form': CreateUserForm(),
#             'appuserform': AppUserForm()
#         }
#         return render(self.request, 'store/signup.html', context)

#     def post(self,*args, **kwargs):
#         userForm = CreateUserForm(data=self.request.POST)
#         appUserForm = AppUserForm(data = self.request.POST)

#         if userForm.is_valid() and appUserForm.is_valid():
#             user = userForm.save(commit=False)
#             email_check = User.objects.filter(email=user.email)
#             if email_check.count():
#                 messages.error(self.request, 'This email already exist. Please signin using the same email or choose another to register')
#                 return render(self.request, 'store/signup.html', {'user_creation_form':userForm, 'appuserform':appUserForm})
            
#             else:
#                 user.username = user.email
#                 name = user.first_name
#                 user.first_name = name.split(' ')[0]
#                 user.last_name = name.split(' ')[-1]
#                 user.save()

#                 appuser = appUserForm.save(commit=False)
#                 appuser.user = user
#                 appuser.save()


#                 messages.success(self.request, 'Your profile has been created, Login to make a purchase')

#                 return HttpResponseRedirect(reverse('store:login'))
        
#         else:
#             messages.error(self.request, 'Something went wrong, Try again')
#             return render(self.request, 'store/signup.html', {'user_creation_form':userForm,'appuserform':appUserForm})

# class SigninView(generic.View):
#     def get(self, *args, **kwargs):
#         return render(self.request, 'store/login.html')

#     def post(self, *args, **kwargs):
#         username = self.request.POST.get('email')
#         password = self.request.POST.get('password')

#         user = authenticate(username=username, password=password)

#         if user:
#             if user.is_active:
#                 login(self.request, user)

#                 return HttpResponseRedirect(reverse('store:cust-account'))
            
#             else:
#                 messages.error(self.request, 'Your account has been deactivated')
#                 return HttpResponseRedirect(reverse('store:login'))

#         else:
#             messages.error(self.request, 'Please use correct email and password combination')
#             return HttpResponseRedirect(reverse('store:login'))

# @login_required
# def signoutview(request):
#     logout(request)
#     return HttpResponseRedirect(reverse('store:products'))

# Products
class CategoryView(View):
    def get(self, *args, **kwargs):
        context={'i':range(0,16)}
        return render(self.request, 'store/products.html')

#add views
# class AddCategory(SuccessMessageMixin,CreateView):
#     model = Category
#     fields = ('__all__')
#     template_name = 'store/add-category.html'
#     success_message = "Category was added successfully"

#     def get_success_url(self, *args, **kwargs):
#         return reverse_lazy('store:add-category')

# class AddProduct(SuccessMessageMixin,CreateView):
#     model = Product
#     fields = ('__all__')
#     template_name = 'store/add-product.html'
#     success_message = "Product was added successfully"

#     def get_success_url(self, *args, **kwargs):
#         return reverse_lazy('store:add-product')

# class ChickensView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Chickens")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/chickens.html', context)

# class ChicksView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Chicks")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/chicks.html', context)

# class EggsView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Eggs")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/eggs.html', context)

# class DucksView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Ducks")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/ducks.html', context)

# class PiecesView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Peices")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/pieces.html', context)

# class EquipmentView(View):
#     def get(self, *args, **kwargs):
#         products = Product.objects.filter(slug="Equipment")
#         paginator = Paginator(products,6)
#         page_number = self.request.GET.get('page')
#         page_obj = paginator.get_page(page_number)
#         context={
#             'page_obj':page_obj,
#         }
#         return render(self.request, 'store/equipment.html', context)

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