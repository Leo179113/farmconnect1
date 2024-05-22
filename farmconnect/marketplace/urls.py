from django.urls import path
from . import views
from .views import product_detail

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('list-product/', views.list_product, name='list_product'),
    path('product-list/', views.product_list, name='product_list'),
    path('search-products/', views.search_products, name='search_products'),
    path('place-order/', views.place_order, name='place_order'),
    path('send-message/', views.send_message, name='send_message'),
    path('product-list', views.product_list, name='product_list'),
    path('product/new/', views.product_create, name='product_create'),
    path('register/', views.register, name='register'),
    path('product/<int:id>/', product_detail, name='product_detail'),
    path('search/', views.search_results, name='search_results'),
]
