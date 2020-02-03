from django.shortcuts import render
from .models import products


def productHome(request):
    data = products.objects.all
    return render(request, 'products/product-home.html', {'products': data})
