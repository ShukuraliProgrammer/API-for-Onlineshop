from django.urls import path
from . import views

urlpatterns = [
    # cart index
    path('carts', views.CartIndex.as_view()),
    path('cartitem', views.CartItemView.as_view()),
    path('cartitem/<int:pk>/', views.CartItemDetailView.as_view()),
]