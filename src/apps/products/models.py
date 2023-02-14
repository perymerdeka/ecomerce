from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

class CategoryModel(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True)
    
    class MPTTMeta:
        order_insertion_by = ['name']


    def __str__(self) -> str:
        return self.name


class BrandModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class ProductModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(BrandModel, on_delete=models.CASCADE)
    category = TreeForeignKey("CategoryModel", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self) -> str:
        return self.name
