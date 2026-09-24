from django.shortcuts import render
from .models import Venue
from main.models import Tehsil
from django.db.models import Q

def venues(request):
    import time 
    time.sleep(1)
    total = Venue.objects.count()
    venues = Venue.objects.exclude(status=0).select_related('tehsil').all()
    tehsil = Tehsil.objects.all()

    query = request.GET.get('search_venues', '').strip()
    sortt_by = request.GET.get('sort_by')

    getteh = request.GET.get('tehsil')
    if getteh and getteh!= "All":
        venues = Venue.objects.exclude(status=0).select_related('tehsil').filter(tehsil__name_en__exact=getteh)
        print(f"Here is venue data {venues}")
    getrp = request.GET.get('rp')
    if getrp and "_" in getrp:
        low, high = getrp.split("_")
        venues = Venue.objects.exclude(status=0).select_related('tehsil').filter(Q(tehsil__name_en=getteh) & Q(room_price__gte=int(low), room_price__lte = int(high)))
    if query:
        venues = Venue.objects.exclude(status=0).select_related('tehsil').filter(Q(name_en__icontains=query) | Q(address_en__icontains=query))
    if sortt_by == "low":
        venues = Venue.objects.exclude(status=0).order_by('room_price')      
    elif sortt_by == "high":
        venues = Venue.objects.exclude(status=0).order_by('-room_price')      
    #else:
     #   venues = Venue.objects.exclude(status=0).select_related('tehsil').all()
        print(f"Tehsil is {getteh}")
        print(f"Final Count: {venues.count()}")
    if request.headers.get('HX-Request') and request.method == "GET":
        return render(request, "partials/venue.html", { 'venues' : venues } )
        
    return render(request, "venues.html", 
                  { 
                      'venues' : venues, 
                      'total' : total , 
                      'tehsil' : tehsil 
                } )
