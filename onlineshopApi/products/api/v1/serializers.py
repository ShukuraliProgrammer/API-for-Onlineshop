from rest_framework import serializers
from products.models import Product, Category
from django.db.models import Max
from django.db.models.functions import Coalesce
from rest_framework.generics import get_object_or_404


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'description', 'slug', 'level', 'total_product_quantity', 'date_created', 'activate')

    def get_total_product(self, obj):
        return obj.total_product
        # slug = serializers.HyperlinkedModelSerializer(
        #     read_only=True,
        #     lookup_field='slug'
        # )

        # lookup_field = 'slug'
    # def get_top_products(self, product):
    #
    #     top = product.product_rating.aggregate(Coalesce(on=Max('quantity'), 0))
    #     data = {
    #         'latest': date_ordered[:3],
    #         'top_products': top,
    #     }
    #     return data
    # def validate_category(self, value):
    #     if self.initial_data.get('parent') is None:
    #         return value
    #     else:
    #         result = self.initial_data.get('parent')
    #         result.delete()
    #         return result

    # def validated_data(self, product):
    #     top_product = product.rating_product.all()
    #     return top_product

    # def validate_not_parent_category(self, value):
    #     if self.initial_data.get('parent') ==None:
    #         return value
    #     return


#
# class CategorySlugSerializer(serializers.ModelSerializer):
#     parent = serializers.SerializerMethodField(read_only=True)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name', 'image', 'slug', 'parent']
#
#     def get_parent(self, instance):
#         try:
#             parent = instance.get_ancestors().last()
#         except IndexError:
#             parent = None
#
#         return CategorySlugSerializer(parent).data
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'price', 'photo', 'description', 'date_created')


class CategoryLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'parent', 'name', 'slug', 'level')

    # def get_category(self, category):
    #     categories = category.objects.filter(level=self.initial_data.pk)
    #     return categories


class Product_Category_Serializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'title', 'price', 'description', 'date_created', 'products')

    # def validate_products(self, validated_data):
    #     category_id = get_object_or_404(Category, id=validated_data.get('category_id'))
    #     return category_id

    # def get_category_id(self, product):
    #     products = product.product.filter(id=self.category).all()
    #
    #     return products
