from django.db import models

# Create your models here.
#create product table
class Product(models.Model):
    product_id = models.AutoField
    product_name= models.CharField(max_length=50)
    category= models.CharField(max_length=50,default="")
    subcategory= models.CharField(max_length=50,default="")
    price= models.IntegerField(default=0)
    desc= models.CharField(max_length=300)
    pub_date=models.DateField()

    image= models.ImageField(upload_to='shop/images',default="")







    def __str__(self):
        return self.product_name
#database for contact page

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    desc = models.TextField()
    pnum = models.CharField(default=0,max_length=20)  # Assuming 'number' is a character field


    def __str__(self):
        return self.name