from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import SrijanApp, SrijanModule
from main.models import ServiceProvider
from .forms import RegistrationForm, LoginForm, ProfileForm, SampleForm, AdduserForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from PIL import Image 
from django.views.decorators.cache import cache_control
from django.views.decorators.vary import vary_on_headers
from django.template.loader import render_to_string
from django.template.loader import get_template
import json 

from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    pass 

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            password = form.cleaned_data.get('password')
            emailid = form.cleaned_data.get('email')
            
            user.set_password(password)
            user.save()
            send_mail("Srijan Registration" , "Your are registered now.", "bharatsamand@gmail.com", [emailid], fail_silently=False)
            return redirect('welcome') 

        else:
            messages.info(request, "Already registered.")

    return render(request, "register.html", { 'form' : form   })

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect("accounts:dashboard")  # home page या dashboard
            else:
                messages.warning(request, "invalid login or password")
                #form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    
    return render(request, "login.html", {"form": form})


def logout_view(request):
    auth_logout(request) # यह सेशन डिलीट कर देगा
    return redirect('home') # लॉगआउट के बाद होम पेज पर भेज दो



@login_required  
def dashboard(request):
    users = User.objects.filter(is_active=1).count()
    providers = ServiceProvider.objects.count()
    ipaddress = request.META["REMOTE_ADDR"]
    context = {
            'users' : users,
            'ipaddress' : ipaddress,
            'providers' : providers
         }
    if request.htmx:
        users = User.objects.filter(is_active=1).count()
        return render(request, "partials/stats.html", {'users':users})
    return render(request, "dashboard.html", context)

@login_required  
def invoice(request):
    iprofile = User.objects.get(id=request.user.id)
    modules = SrijanModule.objects.all()
    apps = SrijanApp.objects.all()
    context = {
        'iprofile' : iprofile,
        'apps' : apps,
        'modules' : modules
    }
    return render(request, "invoice.html", context)


@login_required  
def profile_settings(request):
    profile = User.objects.get(id = request.user.id)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance = profile )
        if form.is_valid():
            done = form.save()
            if done:
                messages.success(request, "it is updated")
    else:
        form = ProfileForm(instance = profile)
    return render(request, "profile_settings.html", {'form' : form, 'profile' : profile  })

@login_required  
@vary_on_headers("HX-Request")
def userprofile(request):
    print(User._meta.get_fields())
    profile = User.objects.get(id=request.user.id)
    if request.headers.get('HX-Request') and request.method == "GET":
       #profile = User.objects.get(id=request.user.id)
       form = ProfileForm(instance = request.user)
       context = {
        'form' : form
        }
       return render(request, "partials/editprofile.html", context)
    return render(request, "userprofile.html", {'profile' : profile })

@login_required  
@vary_on_headers("HX-Request")
def editprofile(request):
    if request.headers.get('HX-Request') and request.method == "POST":
       #profile = User.objects.get(id = request.user.id)
       form = ProfileForm(request.POST, request.FILES, instance = request.user)
       if form.is_valid():
          form.save()
          messages.success(request, "ok saved form")
          #profile = User.objects.get(request.user)
          response = render(request, "partials/myprofile.html", {'profile' : request.user })  
          response['HX-Trigger'] = json.dumps({'success' : "ok success" })
          response.write('<div id="editprofile" hx-swap-oob="true"></div>')
          return response
       else:
          form = ProfileForm(instance=request.user)
          failed = messages.error(request, "failed again" )
          print(f"here is error {form.errors}")
          print(f"here is error {form.non_field_errors}")
          response = render(request, "partials/editprofile.html", {'form' : form} )
          #response['HX-Retarget'] = '#editprofile'
          #response['HX-Reswap'] = 'outerHTML'
          #response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
          return response 
    form = ProfileForm(instance=request.user)
    return render(request, "partials/editprofile.html", {"form": form})

def sample(request):
    if request.method == "POST":
       form = SampleForm(request.POST)
       if form.is_valid():
          form.save()
          messages.success(request," ok saved")
    else:
        form = SampleForm() 
    
    form = SampleForm()
    return render(request, "sample.html", {'form' : form})     


def users(request):
    users = User.objects.get(id=request.user.id)
    context = {
        'users' : users
    }
    return render(request, "users.html", context)

def usersdetails(request, id):
    userobj = get_object_or_404(User, id=id)
    context  = {
        'userobj' : userobj
    }
    return render(request, "partials/userdetails.html", context)

def adduser(request):
    if request.headers.get('HX-Request') and request.method == "GET":
       form = AdduserForm(request.POST)
       context = {
            'form' : form
        }
       return render(request, "partials/adduser.html", context)

@login_required  
@vary_on_headers("HX-Request")
def saveuser(request):
    if request.headers.get('HX-Request') and request.method == "POST":
        user = User.objects.get(pk = request.user.id)
        print(f" yah rha meri id {user}")
        print(f" yah rha meri id {user.id}")
        print(f" yah rha meri id {request.user.id}")
        form = AdduserForm(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            print(f"agar form sahi hai {form}")
            user = User.objects.get(id=request.user.id)
            context = {
                'user' : user
            }
            return render(request, "partials/usersrow.html", context)
        else:
            print(f"errir {form.errors}")
            form = AdduserForm()
            return render(request, "partials/adduser.html", {'form' : form})
