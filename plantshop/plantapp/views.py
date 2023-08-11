# from django.shortcuts import redirect
# from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .forms import ShippingAddressForm
from .models import ShippingAddress
from .models import Product, ReviewRating
from django.shortcuts import render, redirect
from .forms import ReviewForm
from django.shortcuts import render
from .models import Product
from django.shortcuts import render, redirect
from math import ceil
import logging
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import *
from .models import Order, OrderItem, User, Customer
from django.http import JsonResponse
import json
import datetime
from .models import Order, ShippingAddress
from .forms import ReviewForm
from django.db.models import Max
# Create your views here.

# logger = logging.getLogger(__name__)


def home(request):
    # getting product with maximum quantity sold
    maxQuant = Product.objects.aggregate(Max('quantity_sold'))
    maxQuanProd = Product.objects.filter(quantity_sold=maxQuant['quantity_sold__max'])
    context = {'maxQuanProd': maxQuanProd}
    return render(request, 'index.html', context)


def collection(request):
    category = Category.objects.all()
    maintenance = Maintenance.objects.all()
    context = {'category': category, 'maintenance': maintenance}
    return render(request, "collection.html", context)


def collectionview(request, id):
    if(Category.objects.filter(id=id)):

        sort_by = request.GET.get("sort", "price_l2h")
        if sort_by == "price_l2h":
            products = Product.objects.filter(category=id).order_by("price")
        elif sort_by == "price_h2l":
            products = Product.objects.filter(category=id).order_by("-price")
        elif sort_by == "area_l2h":
            products = Product.objects.filter(category=id).order_by("area_req")
        elif sort_by == "area_h2l":
            products = Product.objects.filter(
                category=id).order_by("-area_req")

        name = Category.objects.filter(id=id).first()
        context = {'products': products, 'name': name}
        return render(request, "category.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect("collection")


def collectionviewmaint(request, id):
    if(Maintenance.objects.filter(id=id)):
        sort_by = request.GET.get("sort", "price_l2h")
        if sort_by == "price_l2h":
            products = Product.objects.filter(maintenance=id).order_by("price")
        elif sort_by == "price_h2l":
            products = Product.objects.filter(
                maintenance=id).order_by("-price")
        elif sort_by == "area_l2h":
            products = Product.objects.filter(
                maintenance=id).order_by("area_req")
        elif sort_by == "area_h2l":
            products = Product.objects.filter(
                maintenance=id).order_by("-area_req")
        name = Maintenance.objects.filter(id=id).first()
        context = {'products': products, 'name': name}
        return render(request, "maintenance.html", context)
    else:
        messages.warning(request, "No such category found")
        return redirect("collection")


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
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
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

    context = {'order': order, 'items': items,
               'cartItems': cartItems, 'shipping': False}
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
    print("HELLO BRUH", request.method)
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get('address')
            city = form.cleaned_data.get('city')
            country = form.cleaned_data.get('country')
            shipping_address = ShippingAddress.objects.create(
                customer=customer, order=order, address=address, city=city, country=country)

        # Process the form data and update the order
        # This is just a placeholder and you should replace it with your actual logic
        order.complete = True
        order.save()
        shipping_address.save()
        # Redirect to a success page after completing the order
        return render(request, 'thankyou.html')
    else:
        form = ShippingAddressForm()

    context = {'items': items, 'order': order,
               'cartItems': cartItems, 'shipping': True, 'form': form}
    print("REACHED HERE BRUV")
    return render(request, 'checkout.html', context)


def thankyou_view(request):
    return render(request, 'thankyou.html')


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print("prod ID:", productId)
    print("Action:", action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(
        order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("Item was added", safe=False)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp
    data = json.loads(request.body)  # Corrected 'bdoy' to 'body'

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        
        orderItem = OrderItem.objects.filter(order = order)
        allOrderItem = {'order': orderItem }
        for i in allOrderItem['order']:
            prod = Product.objects.get(product_name=i.product)
            prod.quantity_sold += i.quantity        # increasing the quantity sold
            prod.save()

        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:  # Corrected method call, added parentheses
            order.complete = True
        order.save()

        if order.complete:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],  # Corrected 'address' to 'city'
                # Corrected 'address' to 'state'
                country=data['shipping']['country'],
            )

    else:
        print("User is not logged in..")

    return JsonResponse("Payment complete", safe=False)


def submit_review(request, product_id):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = product_id
            review.user = request.user  # Assuming you have user authentication
            review.save()

            # Get the product object using product_id
            product = get_object_or_404(Product, id=product_id)

            # Redirect to the product's detail page after review submission
            return redirect('product_detail', product_id=product.id)
    else:
        form = ReviewForm()

    return render(request, 'store.html', {'form': form})


def product_list(request):
    products = Product.objects.all()
    reviews = ReviewRating.objects.filter(
        product__in=products, status=True)  # Get reviews for these products
    form = ReviewForm()  # Initialize an empty form for reviews

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.status = True
            review.save()
            # Redirect or render as needed

    context = {
        'products': products,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'store.html', context)


def store(request):
    products = Product.objects.all()
    form = ReviewForm()
    return render(request, 'store.html', {'products': products, 'form': form})


def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})
