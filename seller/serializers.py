from rest_framework import serializers

from seller.models import Seller


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = "__all__"
