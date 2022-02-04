from rest_framework import serializers
from products.models import Product, ProductOption


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'seller',
            'price',
            'image',
            'description',
        ]


class ProductOptionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = ProductOption
        fields = [
            'product',
            'size',
            'color',
            'stock_count',
        ]