from django.contrib import admin
from apps.products.models import Category, Product, ProductVariant, ProductImage

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductVariant)
admin.site.register(ProductImage)