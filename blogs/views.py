import json
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogList
from .forms import BlogForm

# Create your views here.
def list(request):
    blogs = BlogList.objects.filter(created_by=request.user).order_by('-id')
    context = {
        "blogs" : blogs
    }
    return render(request, "blogs.html", context)

def getadd(request):
    form = BlogForm()
    context = {
        "form" : form
    }
    return render(request, "partials/addblogform.html", context)

def savenewblog(request):
    print(1)
    if request.headers.get('HX-Request') and request.method == "POST":
        print(2)
        form = BlogForm(request.POST)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BlogForm(request.POST)
            print(3)
            blog = form.save(commit=False)
            print(f"donor is form save() {blog}")
            blog.created_by = request.user
            print(f"donor is created by {blog.created_by}")
            blog.save()
            print(f"Here the new data {blog}")
            if request.headers.get('HX-Request') and blog:
              #messages.success(request, "your data is saved")
              print(f" here is user id {request.user}")
              myblogs = BlogList.objects.filter(created_by=request.user).order_by('-id')
              #mydonors = Donor.objects.all().order_by('-id')
              print(f"did you get this {myblogs}")
              contextt  = {
                  'x' : blog,
                  #'form'  : form ,
               }
              print(f"here is data of x {contextt}")
              response = render(request, "partials/myblogs.html", contextt)
              response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
              response.write('<div id="addblogform" hx-swap-oob="true"></div>')          
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
       id = BlogList.objects.get(id=id)
       print(f"yah rahi aayi edit id {id}")
       #getid = ServiceProvider.objects.get('id')
       blogs = BlogList.objects.all()
       editform = BlogForm(instance=id)
       return render(request, "partials/editblog.html", { 'editform' : editform, 'blogs' : blogs }  )
    return render(request, "partials/editblog.html", { 'editform' : editform }  )


def saveedit(request, id):
    id = BlogList.objects.get(id=id)
    print(f"page se aayi edit id {id}")
    if request.htmx and request.method == "POST":
        print(2)
        #getins = get_object_or_404(Donor, id= id, created_by=request.user)
        #getins = get_object_or_404(Donor, id=id)
        #donor, created = Donor.objects.get_or_create(created_by=getins)
        #print(f"yah rahi aayi edit wali id {getins}")
        form = BlogForm(request.POST, instance=id)
        print(f"form is valid {form} and errors are {form.errors}")
        if form.is_valid():
            form = BlogForm(request.POST, instance = id)
            print(3)
            blogs = form.save(commit=False)
            #print(f"donor is form save() {donor}")
            blogs.created_by = request.user
            print(f"donor is created by {blogs.created_by}")
            blogs.save()
            #form.save()
            print(f"Here the new data {blogs}")
            #messages.success(request, "your data is saved")
            print(f" here is user id {request.user}")
            mydonors = BlogList.objects.filter(created_by=request.user).order_by('-id')
            #mydonors = Donor.objects.all().order_by('-id')
            print(f"did you get this {mydonors}")
            contextt  = {
                  'x' : blogs,
                  #'form'  : form ,
               }
            print(f"here is data of x {contextt}")
            response = render(request, "partials/myblogs.html", contextt)
            response["HX-Trigger"] = json.dumps({"mysuccess": "डेटा सृजन में सेव हो गया!"})
            response.write('<div id="editblog" hx-swap-oob="true"></div>')          
            return response 

        else:
            form = BlogForm(request.POST, instance=id)
            #failed = messages.error(request, "failed again" )
            print(f"here is error {form.errors}")
            print(f"here is error {form.non_field_errors}")
            response = render(request, "partials/editblog.html", {'editform' : form} )
            response['HX-Retarget'] = '#editblog'
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
            return response 
    else:
        print("yah chal raha ha hai yaar bhai ")
        form = SimpleForm(request.POST)
        return render(request, "partials/editform.html", {'form': form})
