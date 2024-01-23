from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404

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


class WishListUserViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()

    def list(self, request):
        print(request.user)
        queryset = request.user.favourites.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data)

    def create(self, request, pk):

        product = get_object_or_404(Product, pk=pk)
        is_exists = product.favourite_by.filter(id=request.user.id).exists()

        if is_exists:
            return Response(
                {'detail': 'This product has already been added to the favourite list'},
                status=status.HTTP_403_FORBIDDEN
            )

        product.favourite_by.add(request.user)

        return Response({'detail': 'The product has been added to the favourite list successfully'})

    def destroy(self, request, pk):

        product = get_object_or_404(Product, pk=pk)
        is_exists = product.favourite_by.filter(id=request.user.id).exists()

        if not is_exists:
            return Response(
                {'detail': 'This product has not been found in the user\'s favourite list'},
                status=status.HTTP_404_NOT_FOUND
            )

        product.favourite_by.remove(request.user)

        return Response({'detail': 'The product has been removed from the user\'s favourite list'})











