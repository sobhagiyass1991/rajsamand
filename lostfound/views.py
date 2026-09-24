import json
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
from .models import ItemList
from .forms import ItemlistForm

# Create your views here.
def itemlist(request):
    try : 
        list = ItemList.objects.filter(created_by_id=request.user.id)
    except ItemList.DoesNotExist:
        raise Http404("Donors does not exist")
    #donors = not donors 
    context = {
        'list' : list,
    }
    print(f"here is donors {list} ")    
    return render(request, "lostfound.html", context)

def getaddform(request):
    form = ItemlistForm()
    context = {
        'form' : form,
    }
    return render(request, "partials/additemlistform.html", context)

def saveadd(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = ItemlistForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = ItemlistForm(request.POST)
            print(3)
            lostfound = form.save(commit=False)
            print(f"donor is form save() {lostfound}")
            lostfound.created_by = request.user
            print(f"donor is created by {lostfound.created_by}")
            lostfound.save()
            print(f"Here the new data {lostfound}")
            if request.headers.get('HX-Request') and lostfound:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mydonors = ItemList.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mydonors}")
              contextt  = {
                  'x' : lostfound,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/myitems.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="additemlistform" hx-swap-oob="true"></div>')          
              return response 

        else:
            response = render(request, "partials/add-modal.html", {'form' : form} )
            response['HX-Retarget'] = '#my_modal_1'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = 'fail'
            print("yah part chal raha hai" )
            return response 
    else:
        form = SimpleForm()
        return render(request, "partials/mydonors.html", {'form': form})


def testing(request):
    form = ItemlistForm()
    context = {
        'form' : form,
    }
    return render(request, "testing.html", context)

def getedit(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = get_object_or_404(ItemList, id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       editform = ItemlistForm(instance=id)
       return render(request, "partials/editlostfound.html", { 'editform' : editform }  )
    return render(request, "partials/editdonor.html", { 'editform' : editform }  )


def saveeditlostfound(request, id):
    id = get_object_or_404(ItemList, id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = ItemlistForm(request.POST, instance=id)
        print(f"here is the clean data {form.changed_data}")
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = ItemlistForm(request.POST, instance= id)
            print(3)
            requests = form.save(commit=False)
            #print(f"donor is form save() {donation}")
            requests.created_by = request.user
            print(f"donor is created by {requests.created_by}")
            requests.save()
            #form.save()
            print(f"Here the new data {requests}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mydonations = ItemList.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mydonations}")
            contextt  = {
                  'x' : requests,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/myitems.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editlostfoundform" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = RequesttForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editrequest.html", {'editform' : form} )
            response['HX-Retarget'] = '#editrequestform'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})
