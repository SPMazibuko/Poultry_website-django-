from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products, name='all_products'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('equipments', views.equipment, name='equipments'),
    path('lessons', views.lessons, name='lessons'),
    path('products', views.products, name='products'),
    path('quality', views.quality, name='quality'),
    path('eggs', views.eggs, name='eggs'),
    path('login', views.SigninView.as_view(), name='login'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('cust-account', views.AccountView.as_view(), name='cust-account'),
    path('signout', views.signoutview, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),

    #add item
    path('add-category',views.AddCategory.as_view(), name='add-category'),
]
