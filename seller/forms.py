from django.forms import ModelForm
from seller.models import Seller
from seller import util


class SellerForm(ModelForm):
    url_api_produto = util.set_url("192.168.160.3")
    class Meta:
        model = Seller
        
        # produtos = forms.ChoiceField(choices=FormsTools.EmployeesToTuples(Employee.objects.all())) util.get_request()
        fields = "__all__"
        
        # PRODUCTS_CHOICES = [("a", "a")]
        # # get_produtc()
        
        # widgets = {
        #     "product": forms.MultipleChoiceField(
        #         required=False,
        #         widget=forms.CheckboxSelectMultiple,
        #         choices=PRODUCTS_CHOICES,
        #     ),
        # }


