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
]
