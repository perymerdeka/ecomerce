from rest_framework.serializers import ModelSerializer

from apps.products.models import CategoryModel, ProductModel, BrandModel

class CategorySerializer(ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = "__all__"

class ProductSerializer(ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"

class BrandSerializer(ModelSerializer):
    class Meta:
        model = BrandModel
        fields = "__all__"