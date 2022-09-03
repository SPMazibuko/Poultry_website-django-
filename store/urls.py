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
    path('login', views.SigninView.as_view(), name='login'),
    path('signup', views.SignupView.as_view(), name='signup'),
    path('cust-account', views.AccountView.as_view(), name='cust-account'),
    path('signout', views.signoutview, name='signout'),
    path('dashboard', views.dashboard, name='dashboard'),

    #add item
    path('add-category',views.AddCategory.as_view(), name='add-category'),
    path('add-product',views.AddProduct.as_view(), name='add-product'),

    path('chickens',views.ChickensView.as_view(), name='chickens'),
    path('chicks',views.ChicksView.as_view(), name='chicks'),
    path('eggs',views.EggsView.as_view(), name='eggs'),
    path('ducks',views.DucksView.as_view(), name='ducks'),
    path('pieces',views.PiecesView.as_view(), name='pieaces'),
    path('equipments',views.PiecesView.as_view(), name='equipments'),
]
# to save media files during development
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)