from django.contrib import admin
from .models import Restaurants
# Register your models here.

class RestaurantsAdmin(admin.ModelAdmin):
    list_display=("rid","name","location","lat_long")
admin.site.register(Restaurants,RestaurantsAdmin)