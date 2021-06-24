from django.http import request, response

from django.forms import ModelForm
from seller.models import Seller


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        fields = "__all__"
