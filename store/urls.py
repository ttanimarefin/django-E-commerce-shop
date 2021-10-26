from .views import index
from django.urls import path

urlpatterns = [
    path('', index),
    # path('store', store , name='store'),
]
