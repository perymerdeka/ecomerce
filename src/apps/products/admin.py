from django.contrib import admin

# Register your models here.

from .models import CategoryModel, BrandModel, ProductModel

class CategoryModelAdmin(admin.ModelAdmin):
    pass

class BrandModelAdmin(admin.ModelAdmin):
    pass

class ProductModelAdmin(admin.ModelAdmin):
    pass


# register here
admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(BrandModel, BrandModelAdmin)
admin.site.register(ProductModel, ProductModelAdmin)