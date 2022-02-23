from order.models import Order, OrderItem
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'phone', 'region', 'city', 'district', 'state', 'zip_code', 'address')

    def get_full_name(self, obj):
        return obj.full_name

    #
    # class OrderSerializer(serializers.ModelSerializer):
    #     cart_total = serializers.SerializerMethodField()
    #     cart_items = serializers.SerializerMethodField()
    #
    #     class Meta:
    #         model = Order
    #         fields = ['user', 'ordered', 'date_created', 'barcode', 'region', 'city', 'district', 'state',
    #                   'target', 'cart_total', 'cart_items']

    # def get_address(self, value):
    #     if value:
    #         return value
    #     else:

    def get_cart_items(self, obj):
        return obj.cart_items

    def get_cart_total(self, obj):
        return obj.cart_total


class OrderStatisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'status', 'cart_total', 'cart_items' )

    def get_cart_total(self, obj):
        return obj.cart_total

    def get_cart_items(self, obj):
        return obj.cart_items


class OrderItemSerializer(serializers.ModelSerializer):
    order_statis = OrderSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'date_added', 'order_statis']


class OrderItemStatis(serializers.ModelSerializer):
    total_sum = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = ('id', 'total_sum', 'price', 'quantity', 'total_sum')

    def total_sum(self, obj):
        return obj.total_sum
