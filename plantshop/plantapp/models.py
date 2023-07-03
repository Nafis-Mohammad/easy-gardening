from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# create product table


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='authen_profile')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user} Profile'


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()

    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Cart(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_paid = models.BooleanField(default=False)


class CartItems(BaseModel):
    cart_item = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items')
    product_name = models.ForeignKey(
        Product, on_delete=models.SET_NULL, null=True, blank=True)


# database for contact page

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    # Assuming 'number' is a character field
    pnum = models.CharField(default=0, max_length=20)

    def __str__(self):
        return self.name
