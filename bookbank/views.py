import json
from django.shortcuts import render
from .models import Category , BookBankList, BookIssueReturn
from .forms import BookBankForm, BookStatusForm
# Create your views here.

def list(request):
    books = BookBankList.objects.filter(created_by=request.user)
    #books = BookBankList.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books.html', context)

def getadd(request):
    form = BookBankForm()
    context = {
        "form" : form
    }
    return render(request, "partials/addbookform.html", context)

def savenew(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = BookBankForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BookBankForm(request.POST)
            print(3)
            bookbank = form.save(commit=False)
            print(f"donor is form save() {bookbank}")
            bookbank.created_by = request.user
            print(f"donor is created by {bookbank.created_by}")
            bookbank.save()
            print(f"Here the new data {bookbank}")
            if request.headers.get('HX-Request') and bookbank:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mybookbank = BookBankList.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mybookbank}")
              contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/mybooks.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="addbookform" hx-swap-oob="true"></div>')          
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

def getedit(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = BookBankList.objects.get(id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       books = BookBankList.objects.all()
       editform = BookBankForm(instance=id)
       return render(request, "partials/editbook.html", { 'editform' : editform, 'books' : books }  )
    return render(request, "partials/editbook.html", { 'editform' : editform }  )

def saveedit(request, id):
    id = BookBankList.objects.get(id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = BookBankForm(request.POST, instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BookBankForm(request.POST, instance = id)
            print(3)
            bookbank = form.save(commit=False)
            #print(f"donor is form save() {donor}")
            bookbank.created_by = request.user
            print(f"donor is created by {bookbank.created_by}")
            bookbank.save()
            #form.save()
            print(f"Here the new data {bookbank}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mybookbank = BookBankList.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mybookbank}")
            contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/mybooks.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editbook" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = BookBankForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editbook.html", {'editform' : form} )
            response['HX-Retarget'] = '#editbook'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})


def bookstatus(request):
    status = BookIssueReturn.objects.filter(created_by=request.user)
    context = {
        'status' : status
    }
    return render(request, "bookstatus.html", context)

def getaddstatus(request):
    form = BookStatusForm()
    context = {
        "form" : form
    }
    return render(request, "partials/addbookstatusform.html", context)

def savenewstatus(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = BookStatusForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BookStatusForm(request.POST)
            print(3)
            bookbank = form.save(commit=False)
            print(f"donor is form save() {bookbank}")
            bookbank.created_by = request.user
            print(f"donor is created by {bookbank.created_by}")
            bookbank.save()
            print(f"Here the new data {bookbank}")
            if request.headers.get('HX-Request') and bookbank:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              mybookbank = BookBankList.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mybookbank}")
              contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/mybookstatus.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="addbookstatusform" hx-swap-oob="true"></div>')          
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

def geteditstatus(request, id):
    if request.htmx and request.method == "GET":
       #id = get_object_or_404(Donor, id=id, created_by=request.user)
       id = BookIssueReturn.objects.get(id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       books = BookIssueReturn.objects.all()
       editform = BookStatusForm(instance=id)
       return render(request, "partials/editbookstatus.html", { 'editform' : editform, 'books' : books }  )
    return render(request, "partials/editbookstatus.html", { 'editform' : editform }  )

def saveeditstatus(request, id):
    id = BookIssueReturn.objects.get(id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = BookStatusForm(request.POST, instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BookStatusForm(request.POST, instance = id)
            print(3)
            bookbank = form.save(commit=False)
            #print(f"donor is form save() {donor}")
            bookbank.created_by = request.user
            print(f"donor is created by {bookbank.created_by}")
            bookbank.save()
            #form.save()
            print(f"Here the new data {bookbank}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mybookbank = BookBankList.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mybookbank}")
            contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/mybookstatus.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editbookstatus" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = BookBankForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editbook.html", {'editform' : form} )
            response['HX-Retarget'] = '#editbook'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})
