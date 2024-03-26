from django.http import Http404, HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from main.models import Delivery, Product, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request: HttpRequest):
    products = Product.objects.filter(is_active=True)
    paginator = Paginator(products, 9)
    page = request.GET.get('page')
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return HttpResponse(render(request, 'home.html', {
        'products': products,
        'total_price': total_price,
        'items': items
    }))


def products_by_category(request: HttpRequest, category_id: int):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category=category, is_active=True)
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
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

    request.session['add_to_cart_redirect'] = 'products_by_category'
    return HttpResponse(render(request, 'products.html', {
        'category': category,
        'products': products,
        'techniques': techniques,
        'total_price': total_price,
        'items': items
    }))


def products_by_technique(request: HttpRequest, technique: str):
    products = Product.objects.filter(technique=technique, is_active=True)
    category = products.first().category
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    paginator = Paginator(products, 9)
    page = request.GET.get('page')

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    request.session['add_to_cart_redirect'] = 'products_by_technique'
    return HttpResponse(render(request, 'products.html', {
        'products': products,
        'technique': technique,
        'category': category,
        'total_price': total_price,
        'items': items
    }))


def get_product_for_view(product_id: int):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        raise Http404('Товар не найден')

    if not product.is_active:
        raise Http404('Товар не доступен')

    return product


def one_product(request: HttpRequest, product_id: int):
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'one_product.html', {
        'product': get_product_for_view(product_id=product_id),
        'total_price': total_price,
        'items': items
    }))


def add_to_shopping_cart(request: HttpRequest, product_id: int):
    product = get_product_for_view(product_id=product_id)

    if product.count < 1:
        return redirect('one_product', id=product_id)

    shopping_cart = request.session.get('shopping_cart', [])
    product_in_cart = False

    for item in shopping_cart:
        if item['product_id'] == product_id:
            # item['quantity'] += 1
            product_in_cart = True
            break

    if not product_in_cart:
        shopping_cart.append({'product_id': product_id, 'quantity': 1})

    request.session['shopping_cart'] = shopping_cart

    add_to_cart_redirect = request.session.get('add_to_cart_redirect', 'home')

    if add_to_cart_redirect == 'products_by_category':
        return redirect('products_by_category', category_id=product.category.id)
    elif add_to_cart_redirect == 'products_by_technique':
        return redirect('products_by_technique', technique=product.technique)
    else:
        return redirect('home')


def shopping_cart(request: HttpRequest):
    items = request.session.get('shopping_cart', [])
    deliveries = Delivery.objects.all()
    total_price = calculate_total_price(request)

    for item in items:
        item['product'] = Product.objects.get(id=item['product_id'])

    return HttpResponse(render(request, 'shopping_cart.html', {
        'items': items,
        'total_price': total_price,
        'deliveries': deliveries
    }))


def calculate_total_price(request):
    shopping_cart = request.session.get('shopping_cart', [])

    total_price = 0
    for item in shopping_cart:
        product_id = item['product_id']
        quantity = item['quantity']
        product = get_product_for_view(product_id=product_id)
        total_price += product.price * quantity

    return total_price


def delete_from_shopping_cart(request: HttpRequest, product_id: int):
    items = request.session.get('shopping_cart', [])

    for item in items:
        if item['product_id'] == product_id:
            items.remove(item)

    request.session['shopping_cart'] = items
    return redirect('shopping_cart')


def clear_shopping_cart(request: HttpRequest):
    request.session['shopping_cart'] = []
    return redirect('shopping_cart')


def delivery(request: HttpRequest):
    deliveries = Delivery.objects.all()
    total_price = calculate_total_price(request)
    items = request.session.get('shopping_cart', [])
    return HttpResponse(render(request, 'delivery.html', {
        'deliveries': deliveries,
        'items': items,
        'total_price': total_price
    }))


# def profile(request: HttpRequest):
#     total_price = calculate_total_price(request)
#     items = request.session.get('shopping_cart', [])
#     return HttpResponse(render(request, 'profile.html', {
#         'items': items,
#         'total_price': total_price
#     }))