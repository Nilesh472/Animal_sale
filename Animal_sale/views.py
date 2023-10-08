from django.shortcuts import render
from .models import Category1,Category2,Species2,Species1,Contact,Buy
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from Animal_sale.forms import ContactUs,BuyHere



def home(request):
    return render(request, 'Animal/home.html')

def medicine(request):
    return render(request, 'Animal/medicine.html')


def contact(request):
    return render(request, 'Animal/contact.html')

def about(request):
    return render(request, 'Animal/about.html')

def index(request):
    return render(request, 'Animal/index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']

        # Ensure password matches confirmation
        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request, 'Animal/register.html', {
                'message': 'Passwords must match.',
                
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, 'Animal/register.html', {
                'message': 'Username already taken.',
               
            })
        login(request, user)
        return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'Animal/register.html', {
           
        })


def login_view(request):
    if request.method == 'POST':

        # Attempt to sign user in
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'Animal/login.html', {
                'message': 'Invalid username and/or password.',
               
            })
    else:
        return render(request, 'Animal/login.html',  {
          
        })


def logout_view(request):
    logout(request)
    #return HttpResponseRedirect(reverse('index'))
    return redirect('index')


#@login_required(login_url='/login')
def cow_category(request):
    categories = Category1.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'Animal/catogery1.html', context)

#@login_required(login_url='/login')
def buf_category(request):
    categories = Category2.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'Animal/catogery2.html', context)
# Create your views here.

def cow_sp(request,pk):
    species=Species1.objects.all().filter(category1id=pk)
    context={
        'species': species
    }
    return render(request,'Animal/species1.html',context)

def buf_sp(request,pk):
    species=Species2.objects.all().filter(category2id=pk)
    context={
        'species': species
    }
    return render(request,'Animal/species2.html',context)


def contact(request):
    if request.method=='POST':
        fm=ContactUs(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['FirstName']
            mm=fm.cleaned_data['MiddelName']
            lm=fm.cleaned_data['LastName']
            pw=fm.cleaned_data['Password']
            em=fm.cleaned_data['Email']
            ph=fm.cleaned_data['Phone']
            ad=fm.cleaned_data['Address']

            heg=Contact(FirstName=nm,MiddelName=mm,LastName=lm,Password=pw,Email=em,Phone=ph,Address=ad)
            heg.save()
            fm=ContactUs()
    else:
        fm=ContactUs()



    return render(request, 'Animal/contact.html',{'form':fm})

def buy(request):
    if request.method=='POST':
        fm=BuyHere(request.POST)
        if fm.is_valid():
            ac=fm.cleaned_data['AnimalCategory']
            ab=fm.cleaned_data['AnimalBreed']
            yn=fm.cleaned_data['YourName']
            ph=fm.cleaned_data['Phone']
            em=fm.cleaned_data['Email']
            qp=fm.cleaned_data['Quntity']
            pc=fm.cleaned_data['Pricepercattle']
            pn=fm.cleaned_data['Pincode']
            bw=fm.cleaned_data['BuyWithin']
            dc=fm.cleaned_data['description']

            heg=Buy(AnimalCategory=ac,AnimalBreed=ab,YourName=yn,Phone=ph,Email=em,Quntity=qp,Pricepercattle=pc,Pincode=pn,BuyWithin=bw,description=dc,)
            heg.save()
            fm=BuyHere()
    else:
        fm=BuyHere()



    return render(request, 'Animal/buy.html',{'form':fm})
