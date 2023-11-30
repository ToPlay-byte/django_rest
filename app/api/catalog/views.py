from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

