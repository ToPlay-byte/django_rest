from rest_framework import serializers

from .models import Product, Category, ImagesProduct


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = ['path']


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True)

    class Meta:
        model = Product
        exclude = ['favourite_by']


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
