from django.shortcuts import get_object_or_404, render, redirect
from django.http import request, response

from seller.forms import SellerForm
from seller.models import Seller
from seller.serializers import SellerSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet


# Views DRF
class SellerView(ViewSet):
    def get(self, request):
        itens = Seller.objects.all()
        serializer = SellerSerializer(itens, many=True)
        return Response({"articles": serializer.data})
    
    def post(self, request):
        item = request.data.get('name')

        serializer = SellerSerializer(data=item)
        if serializer.is_valid(raise_exception=True):
            item_saved = serializer.save()
        return Response({"success": "Seller '{}' created successfully".format(item_saved.name)})



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
