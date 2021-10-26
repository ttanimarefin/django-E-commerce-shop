from django.shortcuts import render
from .models.product import Product

# Create your views here.
def index(request):
    prds=Product.get_all_products()
    return render(request,'orders/order.html')
    #return render(request,'index.html',{'product':prds})