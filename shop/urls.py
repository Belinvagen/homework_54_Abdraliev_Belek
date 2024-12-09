from django.urls import path
from shop import views

urlpatterns = [
    path('', views.products_view, name='products_view'),
    path('products/', views.products_view, name='products_list'),
    path('products/add/', views.product_add_view, name='product_add_view'),
    path('products/<int:id>/', views.product_view, name='product_detail'),
    path('categories/add/', views.category_add_view, name='category_add_view'),
]
