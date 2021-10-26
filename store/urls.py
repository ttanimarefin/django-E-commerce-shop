from django.urls import path

from .views import home,index,Signup,signup,login

urlpatterns = [
    path('', home.index,name='homepage'),
    path('signup', signup.Signup.as_view(), name='signup'),
    path('login', login.Login.as_view(),name='login')
    
    # path('store', store , name='store'),
]
