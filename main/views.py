from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from main.models import Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def base(request: HttpRequest):
    return HttpResponse(render(request, 'base.html', {}))


def home(request: HttpRequest):
    products = Product.objects.all()
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return HttpResponse(render(request, 'home.html', {
        'products': products
    }))


def products_by_category(request: HttpRequest, category_id: int):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    techniques = set()

    for product in products:
        techniques.add(product.technique)
    techniques = sorted(techniques, key=lambda x: x.lower()) 

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return HttpResponse(render(request, 'products.html', {
        'category': category,
        'products': products,
        'techniques': techniques
    }))


def products_by_technique(request: HttpRequest, technique: str):
    products = Product.objects.filter(technique=technique)
    category = products.first().category
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return HttpResponse(render(request, 'products.html', {
        'products': products,
        'technique': technique,
        'category': category
    }))


def one_product(request: HttpRequest, product_id: int):
    product = Product.objects.get(id=product_id)
    return HttpResponse(render(request, 'one_product.html', {
        'product': product
    }))


def shopping_cart(request: HttpRequest):
    return HttpResponse(render(request, 'shopping_cart.html', {}))


def delivery(request: HttpRequest):
    return HttpResponse(render(request, 'delivery.html', {}))

