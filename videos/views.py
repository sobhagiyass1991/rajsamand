import json
from django.shortcuts import render
from .models import VideoList
from .forms import VideoForm
def list(request):
    videos = VideoList.objects.filter(created_by=request.user)
    context = {
        'videos' : videos
    }
    return render(request, 'videos.html', context)
# Create your views here.

def getadd(request):
    form = VideoForm()
    context = {
        "form" : form
    }
    return render(request, "partials/addvideoform.html", context)

def savenew(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = VideoForm(request.POST,  request.FILES)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = VideoForm(request.POST,  request.FILES)
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
              mybookbank = VideoList.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {mybookbank}")
              contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/myvideos.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="addvideoform" hx-swap-oob="true"></div>')          
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
       id = VideoList.objects.get(id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       books = VideoList.objects.all()
       editform = VideoForm( request.FILES, instance=id)
       return render(request, "partials/editvideo.html", { 'editform' : editform }  )
    return render(request, "partials/editvideo.html", { 'editform' : editform }  )

def saveedit(request, id):
    id = VideoList.objects.get(id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = VideoForm(request.POST,  request.FILES , instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = VideoForm(request.POST, request.FILES, instance = id)
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
            mybookbank = VideoList.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mybookbank}")
            contextt  = {
                  'x' : bookbank,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/myvideos.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editvideo" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = VideoForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editvideo.html", {'editform' : form} )
            response['HX-Retarget'] = '#editvideo'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})

