from django.shortcuts import render
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
    products=Product.get_all_products();
    categories=Category.get_all_products()
    data={}
    data['products']=products
    data['categories']=categories
    # return render(request,'orders/order.html')
    return render(request,'index.html',data)