from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from main.views import calculate_total_price


def profile(request: HttpRequest):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'profile.html', {
        'items': items,
        'total_price': total_price
    }))


def logout(request: HttpRequest):
    request.session.flush()
    return redirect('home')


def profile_info(request: HttpRequest):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'profile_info.html', {
        'items': items,
        'total_price': total_price
    }))


def profile_address(request: HttpRequest):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'profile_address.html', {
        'items': items,
        'total_price': total_price
    }))


def profile_orders(request: HttpRequest):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'profile_orders.html', {
        'items': items,
        'total_price': total_price
    }))