from rest_framework.serializers import ModelSerializer, SlugRelatedField

from .models import Product, Category, ImagesProduct


class ProductSerializer(ModelSerializer):
    images = SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    parent = SlugRelatedField(many=True, slug_field='name', read_only=True)

    class Meta:
        model = Category
        fields = '__all__'
