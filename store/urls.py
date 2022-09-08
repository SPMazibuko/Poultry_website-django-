from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contacts', views.contacts, name='contacts'),
    path('lessons', views.lessons, name='lessons'),
    
    path('products', views.all_products, name='all_products'),
    path('item/<slug:slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/', views.category_list, name='category_list'),

    path('quality', views.quality, name='quality'),
    path('dashboard', views.dashboard, name='dashboard'),
        #add item
    path('add-category',views.AddCategory.as_view(), name='add-category'),
    path('add-product',views.AddProduct.as_view(), name='add-product'),
    
]
# to save media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)