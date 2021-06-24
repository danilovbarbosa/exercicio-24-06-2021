from django import forms

# from django.http import request, response

import requests

from django.forms import ModelForm
from seller.models import Seller


# def get_produtc():
#     r = requests.get("http://172.28.0.3:8000/product/")
#     produtos_dict = r.json()
    
#     print(produtos_dict)

class SellerForm(ModelForm):

    class Meta:
        model = Seller
        fields = "__all__"
        
        PRODUCTS_CHOICES = [("a", "a")]
        get_produtc()
        
        widgets = {
            "product": forms.MultipleChoiceField(
                required=False,
                widget=forms.CheckboxSelectMultiple,
                choices=PRODUCTS_CHOICES,
            ),
        }


