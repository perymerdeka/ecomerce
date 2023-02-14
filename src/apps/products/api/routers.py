from rest_framework.routers import DefaultRouter

from .views import ProductViewSet, CategoryViewSet, BrandViewSet

router = DefaultRouter()

router.register(r"products", ProductViewSet, basename="product")
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"categories", CategoryViewSet, basename="category")

urlpatterns: list = [] + router.urls
