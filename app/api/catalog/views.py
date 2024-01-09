from rest_framework.viewsets import ModelViewSet

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .persmissions import IsAdminOrReadOnly


class ProductViewSet(ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CategoryViewSet(ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)

