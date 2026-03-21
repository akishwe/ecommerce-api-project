import django_filters
from apps.products.models import Product

class ProductFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name="category__id")
    min_price = django_filters.NumberFilter(field_name="variants__price", lookup_expr="gte")
    max_price = django_filters.NumberFilter(field_name="variants__price", lookup_expr="lte")

    class Meta:
        model = Product
        fields = ["category", "min_price", "max_price"]