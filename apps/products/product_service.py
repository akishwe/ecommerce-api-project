from apps.products.models import Product

class ProductService:

    @staticmethod
    def get_filtered_products(filters=None):
        queryset = Product.objects.filter(is_active=True).select_related("category").prefetch_related("variants", "images")

        if not filters:
            return queryset

        category = filters.get("category")
        min_price = filters.get("min_price")
        max_price = filters.get("max_price")
        search = filters.get("search")

        if category:
            queryset = queryset.filter(category_id=category)

        if min_price:
            queryset = queryset.filter(variants__price__gte=min_price)

        if max_price:
            queryset = queryset.filter(variants__price__lte=max_price)

        if search:
            queryset = queryset.filter(name__icontains=search)

        return queryset.distinct()

    @staticmethod
    def get_product_detail(product_id):
        return Product.objects.filter(id=product_id, is_active=True)\
            .select_related("category")\
            .prefetch_related("variants", "images")\
            .first()