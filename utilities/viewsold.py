        if getteh and getteh!= "All":
            utilities = Utility.objects.exclude(status=0).select_related('tehsil').filter(tehsil__name_en__exact=getteh)
            print(f"Here is venue data {venues}")
        #getrp = request.GET.get('rp')
        if getrp and "_" in getrp:
            low, high = getrp.split("_")
            utilities = Utility.objects.exclude(status=0).select_related('tehsil').filter(Q(tehsil__name_en=getteh) & Q(room_price__gte=int(low), room_price__lte = int(high)))
        if sortt_by == "low":
            utilities = Utility.objects.exclude(status=0).order_by('room_price')      
        elif sortt_by == "high":
            utilities = Utility.objects.exclude(status=0).order_by('-room_price')      

        if getteh and getteh!= "All":
            utilities = Utility.objects.exclude(status=0).select_related('subdivision').filter(subdivision__name_en__exact=getteh)
            print(f"Here is venue data {utilities}")
            return render(request, "partials/myutilities.html", { 'utilities' : utilities  })
