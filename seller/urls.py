from django.urls import path, include

from seller import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"seller", views.SellerView, basename='Seller')


urlpatterns = [
    path("api", include(router.urls)),
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
