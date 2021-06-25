import csv

from setup.settings import BASE_DIR

from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from seller.forms import SellerForm
from seller.models import Seller
from seller.serializers import SellerSerializer
from seller.util import get_request, set_url


# Views DRF
class SellerList(APIView):
    def get(self, request, format=None):
        itens = Seller.objects.all()
        serializer = SellerSerializer(itens, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        url_test = set_url("http://192.168.160.3:8000/")
        for i in get_request(url_test):
            if i["id"] is request.data["product"]:
                serializer = SellerSerializer(data=request.data)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(
                        serializer.data, status=status.HTTP_201_CREATED
                    )
                else:
                    return Response(
                        serializer.errors, status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class ProdutoList(APIView):
    def get(self, request, format=None):
        url_test = set_url("http://192.168.160.3:8000/")
        field_names = ["id", "name", "description", "price", "category"]

        produtos_dict = get_request(url_test)
        with open(f"{BASE_DIR}/produtos.csv", "w") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(produtos_dict)

            return Response(status=status.HTTP_201_CREATED)


# Views Django
def create(request):
    formulario = SellerForm(request.POST or None)

    if formulario.is_valid():
        formulario.save()

        return redirect("read")

    context = {
        "title_page": "Criar Seller",
        "post": formulario,
    }
    return render(request, "seller_form.html", context=context)


def read(request):
    list_objetos = Seller.objects.all()

    context = {
        "title_page": "Lista de Sellers",
        "list_objetos": list_objetos,
    }
    return render(request, "seller_list.html", context=context)


def update(request, id):
    post_object = Seller.objects.get(id=id)
    formulario = SellerForm(request.POST or None, instance=post_object)

    if formulario.is_valid():
        formulario.save()

        return redirect("read")
    context = {
        "title_page": "Atualizar Seller",
        "post": formulario,
    }
    return render(request, "seller_form.html", context=context)


def delete(request, id):
    objeto = get_object_or_404(Seller, id=id)
    objeto.delete()
    return redirect("read")
