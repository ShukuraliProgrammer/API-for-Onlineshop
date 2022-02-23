from rest_framework.serializers import ModelSerializer
from .models import (
    Cart,
    CartItem,
)
from products.api.v1.serializers import ProductSerializer


class CartSerializer(ModelSerializer):
    # totalcart = serializers.SerializerMethodField()
    # total_cartitem = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'profile', 'completed']

    # def get_totalcart(self, obj):
    #     return obj.totalcart
    #
    # def get_total_cartitem(self, obj):
    #     return obj.total_cartitem


class CartItemSerializer(ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'cart', 'product', 'quantity', 'created_date']
