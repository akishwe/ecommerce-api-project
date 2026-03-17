from rest_framework import viewsets
from apps.products.models import Category, Product
from apps.products.serializers.product_serializers import (
    CategorySerializer,
    ProductSerializer,
)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.filter(is_active=True)

    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.filter(is_active=True)

    serializer_class = ProductSerializer