from django.urls import path

#from .views import shop_index, groups_list, products_list, orders_list, create_product, create_order
from .views import (
    ShopIndexView,
    GroupsListView,
    ProductDetailsView,
    ProductsListView,
    OrdersListView,
    OrderDetailView,
    create_product,
    create_order)

app_name = "shopapp"

urlpatterns = [
    path("", ShopIndexView.as_view(), name = 'index'),
    path("groups/", GroupsListView.as_view(), name = 'groups_list'),
    path("products/", ProductsListView.as_view(), name = 'products_list'),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name = 'product_details'),
    path("orders/", OrdersListView.as_view(), name = 'orders_list'),
    path("orders/<int:pk>/", OrderDetailView.as_view(), name='order_details'),
    path("products/create", create_product, name='product_create'),
    path("orders/create", create_order, name = 'order_create'),
]
