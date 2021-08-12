from rest_framework import serializers
from store_api.models import *


class ProductDetailSerializer(serializers.ModelSerializer):
    @staticmethod
    def validate_categories(categories):
        if 1 < len(categories) < 11:
            return categories
        raise serializers.ValidationError("Must include 2 to 10 categories")

    @staticmethod
    def validate_price(price):
        if price > 0:
            return price
        raise serializers.ValidationError("Price must be more than 0")

    @staticmethod
    def validate_amount(amount):
        if amount >= 0:
            return amount
        raise serializers.ValidationError("Amount cant be less than 0")

    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
