from django.urls import path
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('product/<slug>/', views.ProductDetailView.as_view(), name='product'),
    path('checkout/', views.checkout, name='checkout'),
]