from django.urls import path
from .views import (
    ProductListView,ProductDetailView, CartItemsView,
    add_product, CartUpdateView, CartDeleteView, InputAddressView
)

app_name='stores'

urlpatterns = [
  path('product_list/', ProductListView.as_view(), name='product_list'),
  path('product_detail/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
  path('product_add_product', add_product, name='add_product'),
  path('cart_items', CartItemsView.as_view(), name='cart_items'),
  path('update_cart/<int:pk>', CartUpdateView.as_view(), name='update_cart'),
  path('delete_cart/<int:pk>', CartDeleteView.as_view(), name='delete_cart'),
  path('input_address', InputAddressView.as_view(), name='input_address'),
  path('input_address/<int:pk>', InputAddressView.as_view(), name='input_address'),
]