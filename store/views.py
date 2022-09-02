from multiprocessing import context
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from store.forms import AppUserForm, CreateUserForm
from .models import Category, Product
from django.contrib import messages
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from django.views.generic import View, CreateView


class AccountView(LoginRequiredMixin,generic.View):
    login_url = '/user/login'
    redirect_field_name = 'user/cust-account/'
    def get(self,*args, **kwargs):
        return render(self.request, 'store/cust-account.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

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

def products(request):
    return render(request, 'store/products.html')

def quality(request):
    return render(request, 'store/quality.html')

def eggs(request):
    products = Product.objects.all()
    return render(request, 'store/eggs.html',{'products': products})

# Registration
class SignupView(generic.View):
    def get(self,*args,**kwargs):
        context = {
            'user_creation_form': CreateUserForm(),
            'appuserform': AppUserForm()
        }
        return render(self.request, 'store/signup.html', context)

    def post(self,*args, **kwargs):
        userForm = CreateUserForm(data=self.request.POST)
        appUserForm = AppUserForm(data = self.request.POST)

        if userForm.is_valid() and appUserForm.is_valid():
            user = userForm.save(commit=False)
            email_check = User.objects.filter(email=user.email)
            if email_check.count():
                messages.error(self.request, 'This email already exist. Please signin using the same email or choose another to register')
                return render(self.request, 'store/signup.html', {'user_creation_form':userForm, 'appuserform':appUserForm})
            
            else:
                user.username = user.email
                name = user.first_name
                user.first_name = name.split(' ')[0]
                user.last_name = name.split(' ')[-1]
                user.save()

                appuser = appUserForm.save(commit=False)
                appuser.user = user
                appuser.save()


                messages.success(self.request, 'Your profile has been created, Login to make a purchase')

                return HttpResponseRedirect(reverse('store:login'))
        
        else:
            messages.error(self.request, 'Something went wrong, Try again')
            return render(self.request, 'store/signup.html', {'user_creation_form':userForm,'appuserform':appUserForm})

class SigninView(generic.View):
    def get(self, *args, **kwargs):
        return render(self.request, 'store/login.html')

    def post(self, *args, **kwargs):
        username = self.request.POST.get('email')
        password = self.request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(self.request, user)

                return HttpResponseRedirect(reverse('store:cust-account'))
            
            else:
                messages.error(self.request, 'Your account has been deactivated')
                return HttpResponseRedirect(reverse('store:login'))

        else:
            messages.error(self.request, 'Please use correct email and password combination')
            return HttpResponseRedirect(reverse('store:login'))

@login_required
def signoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('store:products'))

# Products
class CategoryView(View):
    def get(self, *args, **kwargs):
        context={'i':range(0,16)}
        return render(self.request, 'store/products.html')

class ProductView(View):
    def get(self, *args, **kwargs):
        return render(self.request, 'store/products.html')

#add views
class AddCategory(CreateView):
    model = Category_one
    fields = ('__all__')
    template_name = 'store/add-category.html'