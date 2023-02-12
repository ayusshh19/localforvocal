from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    username=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=10)
    about=models.CharField(max_length=100)
    password=models.CharField(max_length=10)
    
def upload_to(self, filename):
    return 'images/{produser}/{category}/{filename}'.format(produser=self.produser.id,category=self.prodcategory,filename=filename)

category_product=[('shoes','shoes'),('clothes','clothes'),('electronics','electronics'),('food','food'),('handmade','handmade')]
class Addproduct(models.Model):
    prodid=models.AutoField(primary_key=True)
    produser=models.ForeignKey(RegisterUser,on_delete=models.CASCADE)
    prodname=models.CharField(max_length=100)
    prodcategory=models.CharField(max_length=100,choices=category_product)
    prodimage=models.ImageField(upload_to=upload_to, blank=True, null=True)
    prodprice=models.CharField(max_length=100,default=0)
    prodabout=models.CharField(max_length=100)