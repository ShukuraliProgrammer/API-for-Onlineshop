from django.urls import path
from products.api.v1 import views

urlpatterns = [
    # category
    path('categories', views.CategoryView.as_view()),
    path('categories/<int:pk>', views.CategoryUpdateView.as_view()),
    path('categories/<slug:slug>', views.CategoryDetailView.as_view()),
    path('categories/<int:pk>/products', views.Category_ProductsView.as_view()),
    path('categories/level/<int:pk>', views.CategoryLevelView.as_view()),
    path('categories/products/<int:pk>', views.CategoryProductsView.as_view()),

    # product
    path('products', views.ProductView.as_view()),
    path('products/<int:pk>', views.ProductDetailView.as_view()),


    path('latestproducts', views.LatestProductView.as_view()),
]
