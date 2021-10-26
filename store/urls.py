from django.urls import path
from .views import index
from .views.signup import Signup

urlpatterns = [
    path('', index),
    path('signup', Signup, name='signup'),
    
    # path('store', store , name='store'),
]
