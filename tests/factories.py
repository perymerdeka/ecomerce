
from factory.django import DjangoModelFactory

from src.apps.products.models import CategoryModel, BrandModel, ProductModel

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = CategoryModel

    # testing here
    name = "test_category"

class BrandFactory(DjangoModelFactory):
    class Meta:
        model = BrandModel

    # testing here
    name = "test_brand"

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = ProductModel

    # testing here
    name = "test_product"
