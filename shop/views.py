from django.shortcuts import render
from .models import Product
# Create your views here.
from django.http import HttpResponse
from math import ceil

def index(request):
    products = Product.objects.all() 
    print(products)
    n=len(products)
    nslides = n//4+ceil((n/4)-(n//4))
    params = {'no_of_slides':nslides,'range':range(1,nslides),'product':products}
    return render(request, 'shop/index.html', params)

def about(request):
     return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("We are at contact")

def tracker(request):
    return HttpResponse("We are at tracker")

def productView(request):
    return HttpResponse("We are at prodView")

def checkout(request):
    return HttpResponse("We are at checkout")

def search(request):
    return HttpResponse("We are at search")