from rest_framework.routers import DefaultRouter
from apps.products.product_viewsets import CategoryViewSet, ProductViewSet

router = DefaultRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"", ProductViewSet)

urlpatterns = router.urls