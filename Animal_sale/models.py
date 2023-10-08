
from distutils.command.upload import upload
from pyexpat import model
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

class Category1(models.Model):
      title=models.CharField(max_length=200,unique=True)
      description=models.TextField(max_length=500,unique=True)
      image=models.ImageField(upload_to='image/category1/')
      createdAt=models.DateTimeField(auto_now_add=True)
      
      def __str__(self):
            return self.title
      

class Thread(models.Model):
    category1 = models.ForeignKey('Category1', null=True, blank=True, on_delete=models.CASCADE, related_name='threads')

class Category2(models.Model):
      title=models.CharField(max_length=200,unique=True)
      description=models.TextField(max_length=500,unique=True)
      image=models.ImageField(upload_to='image/category2/')
      createdAt=models.DateTimeField(auto_now_add=True)
      


      def __str__(self):
            return self.title


class Thread(models.Model):
    category2 = models.ForeignKey('Category2', null=True, blank=True, on_delete=models.CASCADE, related_name='threads')


class Species1(models.Model):
    category1id=models.ForeignKey(Category1,on_delete=models.CASCADE)
    
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField(max_length=500,unique=True)
    image=models.ImageField(upload_to='images/quiz/')
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Species2(models.Model):
    category2id=models.ForeignKey(Category2,on_delete=models.CASCADE)
    title=models.CharField(max_length=200,unique=True)
    description=models.TextField(max_length=500,unique=True)
    image=models.ImageField(upload_to='images/quiz/')
    createdAt=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

      

class Contact(models.Model):
    FirstName=models.CharField(max_length=70)
    MiddelName=models.CharField(max_length=70)
    LastName=models.CharField(max_length=70)
    Password=models.CharField(max_length=70)
    Email=models.EmailField(max_length=70)
    Phone=models.CharField(max_length=10)
    Address=models.CharField(max_length=100)
    description=models.TextField(max_length=500,unique=True)

PRICE = (
    ("1", "10000-20000"),
    ("2", "20000-40000"),
    ("3", "40000-80000"),
    ("4", "80000-100000"),
    ("5", ">120000"),
    
)
BUY = (
    ("1", "15 day"),
    ("2", "30 day"),
    ("3", ">30 day"),
    
)

class Buy(models.Model):
    AnimalCategory=models.CharField(max_length=70)
    AnimalBreed=models.CharField(max_length=70)
    YourName=models.CharField(max_length=70)
    Phone=models.CharField(max_length=10)
    Email=models.EmailField(max_length=70)
    Quntity=models.CharField(max_length=9)
    Pricepercattle=models.CharField( max_length = 20, choices = PRICE,default = '1')
    Pincode=models.CharField(max_length=100)
    BuyWithin=models.CharField(max_length = 20, choices = BUY,default = '1')
    description=models.TextField(max_length=500,unique=True)


# Create your models here.



# Create your models here.
