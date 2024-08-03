from django.contrib import admin
from django.urls import path

from online_shop import views

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:product_id>', views.product_detail, name='product_detail'),
    path('', views.home, name='home'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/update/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('product/add/', views.product_add, name='product_add'),
]
