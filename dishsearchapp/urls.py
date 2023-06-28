from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home,name='home'),
    path("put_data", views.put_data,name='put_data'),
    path("details/<restaurant_id>", views.restaurant_details,name='restaurant_details'),
    
    
]


