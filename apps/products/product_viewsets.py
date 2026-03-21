from rest_framework import viewsets, status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from apps.products.models import Product, Category
from apps.products.product_serializers import ProductSerializer, CategorySerializer
from apps.products.product_filters import ProductFilter

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name", "description"]
    ordering_fields = ["name", "created_at"]
    ordering = ["name"]

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["name", "description", "category__name"]
    ordering_fields = ["name", "variants__price", "created_at"]
    ordering = ["name"]

    def get_queryset(self):
        return Product.objects.filter(is_active=True)\
            .select_related("category")\
            .prefetch_related("variants", "images")\
            .distinct()

    def retrieve(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if not product:
            return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, context={"request": request})
        return Response(serializer.data)