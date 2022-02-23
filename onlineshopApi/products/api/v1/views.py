from rest_framework import generics
from products.models import Category, Product
from products.api.v1.serializers import CategorySerializer, ProductSerializer, Product_Category_Serializer, CategoryLevelSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser


# Create your views here.

class CategoryView(generics.ListAPIView):
    queryset = Category.objects.filter(parent=None)
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]


class CategoryDetailView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = [IsAuthenticated, IsAdminUser]

    def filter_queryset(self, queryset):
        return queryset.filter(parent__slug=self.kwargs[self.lookup_field])


class CategoryUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class Category_ProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Category_Serializer


class CategoryLevelView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryLevelSerializer
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        data = queryset.filter(level=self.kwargs['pk'])
        return data
    # def put(self, request, pk, format=None):
    #     categor = self.get_object(pk)
    #     serializer = CategoryLevelSerializer(, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LatestProductView(generics.ListAPIView):
    queryset = Product.objects.order_by('-date_created')
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryProductsView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product_Category_Serializer

    def filter_queryset(self, queryset):
        data = queryset.filter(category=self.kwargs['pk'])
        return data
