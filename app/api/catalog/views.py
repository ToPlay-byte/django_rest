from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)


class CategoryViewSet(ModelViewSet):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

