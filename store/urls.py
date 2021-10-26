from django.urls import path
from .views import index
from .views import index,signup,Login

urlpatterns = [
    path('', index,name='homepage'),
    path('signup', signup),
    path('login', Login.as_view())
    
    # path('store', store , name='store'),
]
