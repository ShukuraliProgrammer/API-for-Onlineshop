from django.urls import path, include

urlpatterns = [
    path('v1/', include('products.api.v1.urls')),
]