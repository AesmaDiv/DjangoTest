from rest_framework import serializers
from store_api.models import *


class ItemCreateSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ItemListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name')

