from django.urls import path
from .views import *
from . import views
urlpatterns = [
    # path('', views.HomeView.as_view(), name='home'),
    path('', home, name='home'),
    path('product/', views.ProductView.as_view(), name='product'),
]
