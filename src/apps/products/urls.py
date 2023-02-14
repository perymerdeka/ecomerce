from django.urls import path, include

urlpatterns: list = [
    path("api/", include("apps.products.api.routers"))
]