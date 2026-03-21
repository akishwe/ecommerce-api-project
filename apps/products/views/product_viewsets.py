from rest_framework import viewsets, filters
from apps.products.models import Category, Product
from apps.products.serializers.product_serializers import CategorySerializer, ProductSerializer, ProductVariantSerializer, ProductImageSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description"]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.prefetch_related("variants", "images").all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["name", "description", "category__name"]