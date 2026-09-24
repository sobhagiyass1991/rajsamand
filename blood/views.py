import json
from pydoc import html
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, request
import datetime 
from django.http import Http404
from .models import Donor, Donation, Requestt
from .forms import SimpleForm, DonationForm, DonationForm, RequesttForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.vary import vary_on_headers
from django.db.models import Count, Sum

def donors(request):
    try : 
        donors = Donor.objects.filter(created_by_id=request.user.id)
    except Donor.DoesNotExist:
        raise Http404("Donors does not exist")
    #donors = not donors 
    context = {
        'donors' : donors,
    }
    print(f"here is donors {donors} ")    
    return render(request, "donors.html", context)

def getadd(request):
    form = SimpleForm()
    context = {
        'form' : form,
    }
    return render(request, "partials/adddonorform.html", context)

@login_required  
@vary_on_headers("HX-Request")
def savedonor(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = SimpleForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = SimpleForm(request.POST)
            print(3)
            donor = form.save(commit=False)
            print(f"donor is form save() {donor}")
            donor.created_by = request.user
            print(f"donor is created by {donor.created_by}")
            donor.save()
            print(f"Here the new data {donor}")
            if request.headers.get('HX-Request') and donor:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mydonors = Donor.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mydonors}")
              contextt  = {
                  'x' : donor,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/mydonors.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="adddonorform" hx-swap-oob="true"></div>')          
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

@login_required  
@vary_on_headers("HX-Request")
def getedit(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = get_object_or_404(Donor, id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       editform = SimpleForm(instance=id)
       return render(request, "partials/editdonor.html", { 'editform' : editform }  )
    return render(request, "partials/editdonor.html", { 'editform' : editform }  )


@login_required  
@vary_on_headers("HX-Request")
def saveedit(request, id):
    id = get_object_or_404(Donor, id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = SimpleForm(request.POST, instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            #form = SimpleForm(request.POST, instance= getins)
            print(3)
            donor = form.save(commit=False)
            #print(f"donor is form save() {donor}")
            donor.created_by = request.user
            print(f"donor is created by {donor.created_by}")
            donor.save()
            #form.save()
            print(f"Here the new data {donor}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mydonors = Donor.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mydonors}")
            contextt  = {
                  'x' : donor,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/mydonors.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editdonor" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = SimpleForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editdonor.html", {'editform' : form} )
            response['HX-Retarget'] = '#editdonor'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})


def delete(request, id):
    getobj = Donor.objects.get(id=id)
    print(1)
    if request.method == "DELETE":
        print(2)
        okk = getobj.delete()
        if okk:
            print(3)
            mydonors = Donor.objects.filter(created_by=request.user).order_by('-id')
            response = render(request, "partials/mydonors.html", {'x' : mydonors})
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            return response 


def donations(request):
    try : 
        donations = Donation.objects.filter(created_by_id=request.user.id)
    except Donation.DoesNotExist:
        raise Http404("Donations does not exist")
    #donors = not donors 
    context = {
        'donations' : donations,
    }
    print(f"here is donors {donations} ")    
    return render(request, "donations.html", context)


def getadddonation(request):
    form = DonationForm()
    #form.fields['donorname'].queryset = Donor.objects.filter(created_by=request.user)
    #print(f" yah raha QS ka result {form.fields['donorname'].queryset}")
    context = {
        'form' : form,
    }
    return render(request, "partials/adddonationform.html", context)

def getbloodgroup(request):
#def getbloodgroup(request, id):
    #print(f" yah rahi aane wali {id}")
    if request.htmx and request.method == "GET":
        #print(f" yah rahi aane wali {id}")
        query = request.GET.get("donorname")
        print(f" yah rahi aane wali query {query}")
        getgroup = Donor.objects.get(id__exact=query)
        print(f"here is blood group {getgroup.blood_group}")
        context = {
            'getgroup' : getgroup,
        }
        return render(request, "partials/bgdd.html", context)


def comment(request):
    form = CommentForm()
    print(f"Here is form {form}")
    context= {
        'form' : form
    }
    return render(request, "comment.html", context)


@login_required  
@vary_on_headers("HX-Request")
def savedonation(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = DonationForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = DonationForm(request.POST)
            print(f" here is form donated data {request.POST}")
            print(f" here is form donated data {form.errors}")
            print(3)
            print(f" here is fform.cleaned_data data {form.cleaned_data}")
            print(f" here is form donated data for bg {form.instance.blood_group}")
            donation = form.save(commit=False)
            print(f"donor is form save() {donation}")
            donation.created_by = request.user
            print(f"donor is created by {donation.created_by}")
            donation.save()
            print(f"Here the new data {donation}")
            #print(f"ek aakhri koshish {form.fields["blood_group"]}")
            if request.headers.get('HX-Request') and donation:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mydonors = Donation.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mydonors}")
              contextt  = {
                  'x' : donation,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/mydonations.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="adddonationform" hx-swap-oob="true"></div>')          
              return response 

        else:
            response = render(request, "partials/adddonationform.html", {'form' : form} )
            response['HX-Retarget'] = '#adddonationform'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = 'fail'
            print("yah part chal raha hai" )
            return response 
    else:
        form = SimpleForm()
        return render(request, "partials/mydonors.html", {'form': form})


@login_required  
@vary_on_headers("HX-Request")
def saveeditdonation(request, id):
    id = get_object_or_404(Donation, id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = DonationForm(request.POST, instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = DonationForm(request.POST, instance= id)
            print(3)
            donation = form.save(commit=False)
            #print(f"donor is form save() {donation}")
            donation.created_by = request.user
            print(f"donor is created by {donation.created_by}")
            donation.save()
            #form.save()
            print(f"Here the new data {donation}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mydonations = Donation.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mydonations}")
            contextt  = {
                  'x' : donation,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/mydonations.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editdonationform" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = DonationForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editdonation.html", {'editform' : form} )
            response['HX-Retarget'] = '#editdonationform'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})


@login_required  
@vary_on_headers("HX-Request")
def geteditdonation(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = get_object_or_404(Donation, id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       editform = DonationForm(instance=id)
       return render(request, "partials/editdonation.html", { 'editform' : editform }  )
    return render(request, "partials/editdonor.html", { 'editform' : editform }  )


def requests(request):
    try : 
         requests =  Requestt.objects.filter(created_by_id=request.user.id)
    except Requestt.DoesNotExist:
        raise Http404("Donations does not exist")
    #donors = not donors 
    context = {
        'requests' : requests,
    }
    print(f"here is donors {requests} ")    
    return render(request, "requests.html", context)

@login_required  
@vary_on_headers("HX-Request")
def geteditrequests(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = get_object_or_404(Requestt, id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       editform = RequesttForm(instance=id)
       return render(request, "partials/editrequest.html", { 'editform' : editform }  )
    return render(request, "partials/editdonor.html", { 'editform' : editform }  )


@login_required  
@vary_on_headers("HX-Request")
def saveeditrequests(request, id):
    id = get_object_or_404(Requestt, id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = RequesttForm(request.POST, instance=id)
        print(f"here is the clean data {form.changed_data}")
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = RequesttForm(request.POST, instance= id)
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
            mydonations = Requestt.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mydonations}")
            contextt  = {
                  'x' : requests,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/myrequests.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editrequestform" hx-swap-oob="true"></div>')          
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


def getbloodgroupvolume(request):
#def getbloodgroup(request, id):
    #print(f" yah rahi aane wali {id}")
    if request.htmx and request.method == "GET":
        #print(f" yah rahi aane wali {id}")
        query = request.GET.get("blood_group")
        print(f" yah rahi aane wali query {query}")
        getgroup = Donation.objects.filter(blood_group__contains=query).aggregate(Sum("volume"))
        print(f"here is blood group {getgroup}")
        context = {
            'getgroup' : getgroup,
        }
        return render(request, "partials/bgddv.html", context)


def getaddrequest(request):
    form = RequesttForm()
    #form.fields['donorname'].queryset = Donor.objects.filter(created_by=request.user)
    #print(f" yah raha QS ka result {form.fields['donorname'].queryset}")
    context = {
        'form' : form,
    }
    return render(request, "partials/addrequestform.html", context)

@login_required  
@vary_on_headers("HX-Request")
def saverequest(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = RequesttForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = RequesttForm(request.POST)
            print(f" here is form donated data {request.POST}")
            print(f" here is form donated data {form.errors}")
            print(3)
            print(f" here is fform.cleaned_data data {form.cleaned_data}")
            print(f" here is form donated data for bg {form.instance.blood_group}")
            requestt = form.save(commit=False)
            print(f"donor is form save() {requestt}")
            requestt.created_by = request.user
            print(f"donor is created by {requestt.created_by}")
            requestt.save()
            print(f"Here the new data {requestt}")
            #print(f"ek aakhri koshish {form.fields["blood_group"]}")
            if request.headers.get('HX-Request') and requestt:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mydonors = Requestt.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mydonors}")
              contextt  = {
                  'x' : requestt,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/myrequests.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="addrequestform" hx-swap-oob="true"></div>')          
              return response 

        else:
            response = render(request, "partials/addrequestform.html", {'form' : form} )
            response['HX-Retarget'] = '#addrequestform'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = 'fail'
            print("yah part chal raha hai" )
            return response 
    else:
        form = SimpleForm()
        return render(request, "partials/mydonors.html", {'form': form})

