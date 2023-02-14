from rest_framework.viewsets import ModelViewSet


from .serializers import CategorySerializer, ProductSerializer, BrandSerializer
from apps.products.models import CategoryModel, ProductModel, BrandModel


class CategoryViewSet(ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class BrandViewSet(ModelViewSet):
    queryset = BrandModel.objects.all()
    serializer_class = BrandSerializer
