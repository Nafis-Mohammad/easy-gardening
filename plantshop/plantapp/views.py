# from django.shortcuts import redirect
# from django.shortcuts import render
from django.shortcuts import render, redirect
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .models import Order, OrderItem, User, Customer
from django.http import JsonResponse
import json


# Create your views here.


def home(request):
    return render(request, 'index.html')


def product(request):
    current_user = request.user
    print(current_user)
    # all product
    allProd = []
    # category
    catprod = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprod}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        slide = n // 4 + ceil((n/4)-(n//4))
        allProd.append([prod, range(1, slide), slide])

    para = {'allProd': allProd}
    return render(request, 'product.html', para)

# contact page


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        desc = request.POST.get("desc")
        pnumber = request.POST.get("pnumber")
        query = Contact(name=name, email=email, desc=desc, pnum=pnumber)
        query.save()
        messages.info(request, "We will get back to you soon..")
        return render(request, 'contact.html')

    return render(request, 'contact.html')


def add_to_cart(request, slug):
    product_name = product_name.objects.get(slug=slug)
    variant = request.GET.get('variant')
    user = request.user
    cart, _ = Order.objects.get_or_create(user=user, is_paid=False)

    return redirect('/')


def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {
        'products': products,
        'cartItems': cartItems
    }
    return render(request, 'store.html', context)


def carts(request):
    order = None  # Initialize the order variable
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    context = {'order': order, 'items': items, 'cartItems': cartItems}
    return render(request, 'carts.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']

    if request.method == 'POST':
        # Process the form data and update the order
        # This is just a placeholder and you should replace it with your actual logic
        order.complete = True
        order.save()
        # Redirect to a success page after completing the order
        return redirect('order-success')

    context = {'items': items, 'order': order, 'cartItems': cartItems}
    return render(request, 'checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("prod ID:", productId)
    print("Action:", action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer = customer, complete = False)
    orderItem, created = OrderItem.objects.get_or_create(order = order, product = product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)