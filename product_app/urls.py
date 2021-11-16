from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('product/', views.ProductView.as_view(), name='product'),
    path('single-product/<int:product_id>', views.SinglepProductView.as_view(), name='single_product'),
    path('privacy', privacy, name='privacy'),
]
