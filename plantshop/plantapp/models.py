from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
# create product table


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='authen_profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False, blank=False)
    category_slug = models.CharField(max_length=150, null=False, blank=False)
    category_image = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)       # CHANGE THIS
    category_description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.category_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    

class Maintenance(models.Model):
    maintenance_name = models.CharField(max_length=50, null=False, blank=False)
    maintenance_image = models.ImageField(upload_to='shop/images', default="", null=True, blank=True)       # CHANGE THIS
    maintenance_description = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return self.maintenance_name
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE, default=None)
    area_req = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


# database for contact page

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    # Assuming 'number' is a character field
    pnum = models.CharField(default=0, max_length=20)

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.transaction_id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        ordertimes = self.orderitem_set.all()
        total = sum([item.quantity for item in ordertimes])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(
        Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


# Creating the Wish model
class Wish(models.Model):

    # Defining the fields of the model
    wishtitle = models.CharField(max_length=250, unique=True)
    wish = models.CharField(max_length=1000)
    link = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    is_achieved = models.BooleanField(default=False, blank=True)
    image = models.ImageField(upload_to='images/')

    # Defining the string representation of the model
    def __str__(self):
        return self.wishtitle