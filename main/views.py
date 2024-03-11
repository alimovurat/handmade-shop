from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest):
    return HttpResponse(render(request, 'home.html', {}))


def paintings(request: HttpRequest):
    return HttpResponse(render(request, 'paintings.html', {}))


def stuffed_toys(request: HttpRequest):
    return HttpResponse(render(request, 'stuffed_toys.html', {}))


def brooches(request: HttpRequest):
    return HttpResponse(render(request, 'brooches.html', {}))


def product(request: HttpRequest):
    return HttpResponse(render(request, 'product.html', {}))


def shopping_cart(request: HttpRequest):
    return HttpResponse(render(request, 'shopping_cart.html', {}))


def delivery(request: HttpRequest):
    return HttpResponse(render(request, 'delivery.html', {}))