from enum import Flag
from django.core.checks.messages import ERROR

from django.db.models.expressions import Value
from django.db.utils import Error
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from store.models.customer import Customer
from .models.product import Product
from .models.category import Category
from django.core.exceptions import ValidationError

# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_products()
    categoryID = request.GET.get('category')
    if categoryID:
        products = Product.get_all_products_by_categoryid(categoryID)
    else:
        products = Product.get_all_products()
    data = {}
    data['products'] = products
    data['categories'] = categories
    # return render(request,'orders/order.html')
    return render(request, 'index.html', data)


def validateCustomer(customer):
    _ErrorMessage = None
    if(not customer.first_name):
        _ErrorMessage = "First Name Required !"
    elif len(customer.first_name):
        _ErrorMessage = 'First Name must be 4 char long'
    elif customer.isExists():
        _ErrorMessage = 'Email address Already registered'

    return _ErrorMessage


def registerUser(request):

    postData = request.POST
    first_name = postData.get('firstname')
    last_name = postData.get('lastname')
    phone = postData.get('phone')
    email = postData.get('email')
    password = postData.get('password')

    value = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone,
        'email': email

    }
    _ErrorMessage = None

    customer = Customer(first_name=first_name,
                        last_name=last_name,
                        phone=phone,
                        email=email,
                        password=password)

    error_message = validateCustomer(customer)

    # save
    if not _ErrorMessage:
        print(first_name, last_name, phone, email, password)

        customer.register()

        return redirect('homepage')
    else:
        data = {
            'error': _ErrorMessage,
            'values': value
        }
    filter_horizontal = ()
    return render(request, 'signup.html', data)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    else:
        return registerUser(request)
        # vali




def login(request):
    if request.method=='GET':
        return render(request,'login.html')

    else:
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        ErrorMessage=None
        if customer:

            flag=  password(password)
            if flag:
                return redirect('homepage')
            else:
                ErrorMessage='Email or Pass invalid'
        else:
            ErrorMessage='Email or Pass invalid'

        return render(request,'login.html',{'error':ErrorMessage})
    