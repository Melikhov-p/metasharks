from sharks_api.models import *
from rest_framework import serializers

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'name')

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name')

class ModelSerializer(serializers.ModelSerializer):
    # brand = serializers.StringRelatedField()

    class Meta:
        model = Model
        fields = ('id', 'name', 'brand')

class OrderSerializer(serializers.ModelSerializer):
    # brand = serializers.StringRelatedField()
    # model = serializers.StringRelatedField()
    # color = serializers.StringRelatedField()
    class Meta:
        model = Order
        fields = ('id', 'brand', 'model', 'color', 'date')