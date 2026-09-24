from django.shortcuts import render, get_object_or_404, redirect
import json
from .models import LssemsService, ServiceProvider
from .forms import ServiceForm
from django.core.paginator import Paginator

def lssemsedit(request, id):
    if request.htmx and request.method == "GET":
       id = get_object_or_404(ServiceProvider, id= id, user=request.user)
       #getid = ServiceProvider.objects.get('id')
       editform = ServiceForm(instance=id)
       return render(request, "partials/editservice.html", { 'editform' : editform }  )

    if request.htmx and request.method == "POST":
       id = get_object_or_404(ServiceProvider, id= id, user=request.user)
       print(f"yaha raha villain {id}")
       #getid = ServiceProvider.objects.get('id')
       form = ServiceForm(request.POST, instance=id)
       if form.is_valid():
          obj = form.save(commit=False)
          obj.user = request.user
          obj.save()
          print(f"Here the new data {obj}")
          if request.headers.get('HX-Request') and obj:
              #messages.success(request, "your data is saved")
              myservices = ServiceProvider.objects.filter(user=request.user).order_by('-id')
              print(f"did you get this {myservices}")
              contextt  = {
                  'x' : obj,
                  #'form'  : form ,
               }
              response = render(request, "partials/myservices.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              return response 
            
       else:
            form = ServiceForm(request.POST)
            failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/addserviceform.html", {'form' : form} )
            response['HX-Retarget'] = '#addserviceform'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
      


def lssems(request, *args, **kwargs):
    #profile = User.objects.get(id=request.user.id)
    myservices = ServiceProvider.objects.filter(user=request.user).all()
    editid = request.GET.get('editid')
    print(f"here is my edit id {editid}")
    if request.headers.get('HX-Request'):
        if request.method == "GET" and editid :
            print(f"here is args {args}")
            print(f"here is kwargs {kwargs}")
            print(f"GET वाला डेटा: {request.GET}")
            print(f"POST वाला डेटा: {request.POST}")
            getdata = get_object_or_404(ServiceProvider, id = editid)
            profile = User.objects.get(id=request.user.id)
            editform = ServiceForm(request.POST, instance = getdata)
            print(f"here is id i get for edit{editid}")
            print(f"here is another form for efir {editform}")
            return render(request, "partials/editservice.html", { 'editform' : editform , 'getdata' : getdata }  )


    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
           obj = form.save(commit=False)
           obj.user = request.user
           obj.save()
           print(f"Here the new data {obj}")
           if request.headers.get('HX-Request') and obj:
              #messages.success(request, "your data is saved")
              myservices = ServiceProvider.objects.filter(user=request.user).order_by('-id')
              print(f"did you get this {myservices}")
              contextt  = {
                  'x' : obj,
                  #'form'  : form ,
               }
              response = render(request, "partials/myservices.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              return response 
            
        else:
              form = ServiceForm(request.POST)
              failed = messages.error(request, "failed again" )
              print(f"here is error {form.errors}")
              print(f"here is error {form.non_field_errors}")
              response = render(request, "partials/addserviceform.html", {'form' : form} )
              response['HX-Retarget'] = '#addserviceform'
              response['HX-Reswap'] = 'outerHTML'
              response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
              return response 

    if request.method == "GET":
       form = ServiceForm()
       if request.headers.get('HX-Request'):
           return render(request, "partials/addserviceform.html", {'form' : form})

    page_obj = Paginator(myservices ,10)
    page_obj = page_obj.get_page(request.GET.get('page'))
    print(f"page ko dikhao {page_obj}")
    context = {
        'page_obj' : page_obj
    }
    return render(request, "lssems.html", context)

