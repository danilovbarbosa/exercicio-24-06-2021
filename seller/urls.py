from django.urls import path

from seller import views


urlpatterns = [
    path("seller/", views.SellerList.as_view()),
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
