from django.shortcuts import render
from .models import UtilityCategory, Utility
from main.models import Tehsil
from django.db.models import Q

# Create your views here.
def getautility(request, id):
    id = UtilityCategory.objects.get(id=id)
    categories = UtilityCategory.objects.all()
    tehsil = Tehsil.objects.all()    
    print(f" here are the data {id}")
    getcat = request.GET.get("id")
    print(f" here are the get cat data {getcat}")
    utility = Utility.objects.filter(category_id=id)
    print(f" here are the data {utility}")
    context = {
        "categories" : categories,
        "utilities": utility,
        "tehsil": tehsil
    }
    return render(request, "partials/getautility.html", context)

def venues(request):
    #if request.headers.get('HX-Request') and request.method == "GET":
        import time 
        time.sleep(1)
        total = Utility.objects.count()
        venues = Utility.objects.exclude(status=0).select_related('tehsil').all()
        tehsil = Tehsil.objects.all()
        utilities = Utility.objects.all()

        getteh = request.GET.get('tehsil')
        query = request.GET.get('search_utility', '').strip()
        print(f"Here is the query {getteh}")
        print(f"Here is the query {query}")
        if getteh:
            utilities = Utility.objects.exclude(status=0).select_related('subdivision').filter(subdivision__name_en__exact=getteh)
            print(f"Here is the 1st part {utilities}")
        if query:
            utilities = Utility.objects.exclude(status=0).select_related('subdivision').filter(
                 Q(subdivision__name_en__exact=getteh) &           
                 Q(name_en__icontains=query) | 
                 Q(address__icontains=query) |
                 Q(name_hi__icontains=query)
                )
            print(f"Here is the 2nd part {utilities}")
            return render(request, "partials/myutilities.html", {
                             'utilities' : utilities  
                        })
        elif(query == ""):
            #utilities = Utility.objects.exclude(status=0).all()
            print(f"here is the khaali query {utilities}")  
            return render(request, "partials/myutilities.html", {
                             'utilities' : utilities  
                        })


        return render(request, "partials/myutilities.html", { 'utilities' : utilities  } )