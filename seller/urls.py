from django.urls import path, include

from seller import views

from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('seller/', views.SellerList.as_view()),
    path("create/", views.create, name="create"),
    path("read/", views.read, name="read"),
    path("update/<int:id>", views.update, name="update"),
    path("delete/<int:id>", views.delete, name="delete"),
]
