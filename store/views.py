from django.http.response import HttpResponse
from django.shortcuts import render

from store.models.customer import Customer
from .models.product import Product
from .models.category import Category

# Create your views here.
def index(request):
    products=None
    categories=Category.get_all_products()
    categoryID=request.GET.get('category')
    if categoryID:
        products=Product.get_all_products_by_categoryid(categoryID)
    else:
            products=Product.get_all_products();
    data={}
    data['products']=products
    data['categories']=categories
    # return render(request,'orders/order.html')
    return render(request,'index.html',data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        postData = request.POST
        first_name=postData.get('firstname')
        last_name=postData.get('lastname')
        phone=postData.get('phone')
        email=postData.get('email')
        password=postData.get('password')
        customer=Customer(first_name=first_name,
                          last_name=last_name,
                          phone=phone,
                          email=email,
                          password=password
        
        
        
        )
        customer.register()

        return HttpResponse("signup")
    