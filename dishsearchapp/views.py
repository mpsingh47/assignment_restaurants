from django.shortcuts import render
import csv,os,json,re
from .models import Restaurants
from django.http.response import HttpResponse

# Create your views here.

def home(request):
    # return HttpResponse('This is Home Page')
    if request.method=='GET':
        context={}
        return render(request,'home.html',context)
    
    elif request.method=='POST':
        dishsearched=request.POST.get("searchdish")
        # print(dishsearched)
        final_restaurants_list=[]
        restaurants_all = Restaurants.objects.all()
        for restaurant in restaurants_all:
            json_items = json.loads(restaurant.items)
            
            r = re.compile(f".*{dishsearched}.*" ,  re.IGNORECASE)
            
            matches = {key: value for key, value in json_items.items() if r.search(str(key) ) }

            print(matches)

            if (len(matches)>0):
                single_restaurant_json=dict()
                single_restaurant_json["rid"]=restaurant.rid
                single_restaurant_json["name"]=restaurant.name
                single_restaurant_json["location"]=restaurant.location
                single_restaurant_json["items_searched"]=matches 
                single_restaurant_json["lat_long"]=restaurant.lat_long
                single_restaurant_json["full_details"]=json.loads(restaurant.full_details)

                final_restaurants_list.append(single_restaurant_json)
        print(final_restaurants_list , len(final_restaurants_list))


              

        # print(type(res[0]),type(res[0].items))
        # res = Restaurants.objects.filter(items__icontains={'key__contains': 'dish'})
        # print(res)

        context={
            'dishsearched':dishsearched,
            'final_restaurants_list':final_restaurants_list
        }

        return render(request,'home.html',context)
    else:
        return HttpResponse("some error")

def put_data(request):
    try:
        with open("restaurants_small.csv") as csvfile:
            csvreader = csv.reader(csvfile,delimiter=",")
            next(csvreader)
            for row in csvreader:
                
                data={
                    "rid":int(row[0]),
                    "name":row[1],
                    "location":row[2],
                    "items":row[3],
                    "lat_long":row[4],
                    "full_details":row[5]
                }
                if row[5]=="" or row[5] is None:
                    data["full_details"]="{}"
                restaurants_obj = Restaurants(**data)
                restaurants_obj.save()
        
        return HttpResponse(f"""<h1>Data transeferred to model db sqlite</h1><br><a href="{request.path[:-8]}">Home</a> """)
    except Exception as e:
        return HttpResponse(f"Already Done <br> Error.. {e}")
    
def restaurant_details(request,restaurant_id):
    try:

        res = Restaurants.objects.get(rid = restaurant_id)
        context={
            "rid":res.rid,
            "name":res.name,
            "city":res.location,
            "items":res.items,
            "lat_long":res.lat_long,
            "full_details":res.full_details
        }
        return render(request,'single_restaurant_detail.html',context)
    except Exception as e:
        return HttpResponse(f"Error {e}")

# HttpResponseRedirect(reverse("news-year-archive", args=(year,)))
def about(request):
    return render(request,'home.html')
    # return HttpResponse('This is ABout')


