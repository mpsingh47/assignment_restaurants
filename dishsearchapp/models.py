from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class Restaurants(models.Model):

    rid=models.IntegerField(unique=True)
    name= models.CharField( max_length=100)
    location=models.CharField( max_length=100)
    items = models.JSONField(encoder=None, decoder=None, default=dict)
    # item_names=ArrayField(models.CharField(max_length=100), blank=True,null=True)
    # item_price=ArrayField(models.FloatField(), blank=True,null=True)
    lat_long = models.CharField( max_length=50,blank=True, null=True)
    full_details = models.JSONField( encoder=None, decoder=None,default=dict,blank=True)
    
    class Meta:
        db_table = 'restaurants_db'
        verbose_name_plural = "Restaurants DB"

  

   

    