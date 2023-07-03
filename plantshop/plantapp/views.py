from django.shortcuts import render
<<<<<<< HEAD
from plantapp.models import Product,Contact
from math import ceil
from django.contrib import messages
# Create your views here.
def home(request):
     return render(request,'index.html')
def product(request):
    current_user=request.user
    print(current_user)
    #all product
    allProd=[]
    #category
    catprod= Product.objects.values('category','id')
    cats={item['category'] for item in catprod}

    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n = len(prod)
        slide=n // 4+ ceil((n/4)-(n//4))
        allProd.append([prod,range(1,slide),slide])

    para={'allProd':allProd}
    return render(request,'product.html',para)

# contact page
def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        desc=request.POST.get("desc")
        pnumber=request.POST.get("pnumber")
        query=Contact(name=name,email=email,desc=desc,pnum=pnumber)
        query.save()
        messages.info(request,"We will get back to you soon..")
        return render(request,'contact.html')

    return render(request,'contact.html')


=======
from django.shortcuts import render, redirect
from plantapp.models import Product, Contact
from math import ceil
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Cart, CartItems
from django.http import HttpResponse

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
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    return redirect('/')


def store(request):
    context = {}
    return render(request, 'store.html', context)


def carts(request):
    context = {}
    return render(request, 'carts.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)
>>>>>>> a1cfe3135fb2b4a09571e81750125c86d237723d
