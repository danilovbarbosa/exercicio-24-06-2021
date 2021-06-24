from django.contrib import admin
from seller.models import Seller


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    pass
