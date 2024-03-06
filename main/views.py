from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest):
    return HttpResponse(render(request, 'home.html', {}))


def product(request: HttpRequest):
    return HttpResponse(render(request, 'product.html', {}))


def shopping_cart(request: HttpRequest):
    return HttpResponse(render(request, 'shopping_cart.html', {}))