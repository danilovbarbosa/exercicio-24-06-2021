from django.shortcuts import render


def home(request):
    context = {}
    return render(request, "base.html", context=context)
