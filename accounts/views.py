from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import SrijanApp, SrijanModule
#, Teacher, Jobslist, School, Student, SubjectMark
from localservices.models import ServiceProvider
from .forms import RegistrationForm, LoginForm, ProfileForm, SampleForm,  UserRegistrationForm
#, TeacherForm, JobpostForm, SchoolDetailsForm, StudentForm, SubjectMarksForm
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
          form = ProfileForm(request.POST, instance=request.user)
          response = render(request, "partials/editprofile.html", {'form' : form} )
          response['HX-Retarget'] = '#editprofile'
          response['HX-Reswap'] = 'outerHTML'
          response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
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


@login_required
def users(request):
    print("Logged in user id:", request.user.id)
    users = User.objects.filter(parent_id=request.user.id)
    #users = User.objects.all()
    teacher = Teacher.objects.all()
    print(f"mere user hai {users}")
    #users = User.objects.filter(parent_id = request.user.id)
    context = {
        'users' : users,
        'teacher' : teacher
    }
    return render(request, "users.html", context)

def usersdetails(request, id):
    userobj = get_object_or_404(User, id=id)
    context  = {
        'userobj' : userobj
    }
    return render(request, "partials/userdetails.html", context)

@login_required  
@vary_on_headers("HX-Request")
def adduser(request):
    if request.headers.get('HX-Request') and request.method == "GET":
       #form = AdduserForm(request.POST)
       form = UserRegistrationForm()
       form = context = {
            'form' : form
        }
       return render(request, "partials/adduser.html", context)

@login_required  
@vary_on_headers("HX-Request")
def saveuser(request):
    form = UserRegistrationForm()
    if request.headers.get('HX-Request') and request.method == "POST":
        getuser = User.objects.get(id = request.user.id)
        print(f"yah hai user {getuser}")
        form = UserRegistrationForm(request.POST, request.FILES, instance=getuser)
        if form.is_valid():
            userr = form.save(commit=False)
            userr.parent = request.user
            password = form.cleaned_data.get('password')
            userr.set_password(password)
            form.save()
            #users = User.objects.filter(id=request.user.id).order_by('-id')
            context = {
                'users' : userr,
            }
            #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
            return render(request, "partials/usersrow.html", context)
        else:
            response = render(request, "partials/adduser.html", {'form' : form} )
            response["HX-Retarget"] = "#adduser"
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = json.dumps({"failed": "Form me error hai"})
            #response['HX-Trigger-After-Settle'] = 'user_failed'
            return response 
    return render(request, "partials/adduser.html", {'form' : form})

@login_required  
@vary_on_headers("HX-Request")
def getteacher(request, id):
    if request.headers.get('HX-Request') and request.method == "GET":
        userobj = get_object_or_404(User, id=id)
        #tobj = get_object_or_404(Teacher, child=userobj)
        form = TeacherForm(instance=userobj)   # ✅ FIX
        print(f"yah rahi id {id}")
        print(f"yah rahi form ins id {form.instance.id}")
        print(f"yah rahi form {form}")
        return render(request, "partials/teacherform.html", {
            'form': form,
            'instance': userobj      # 👈 IMPORTANT
        })


@login_required  
@vary_on_headers("HX-Request")
def saveteacher(request, id):
    if request.headers.get('HX-Request') and request.method == "POST":
       getuser = get_object_or_404(User , id = id)       
       print(f"yah raha user {getuser}")
       teacher, created = Teacher.objects.get_or_create(child=getuser)
       form = TeacherForm(request.POST, instance=teacher)
       #form = TeacherForm(request.POST, request.FILES, instance = getuser)
       print(f"yah rahi id {getuser}")
       print(f"yah rahi id {form}")
       print("URL id:", id)
       print("Editing user:", getuser.id)
       print("Logged user:", request.user.id)
       if form.is_valid():
         teacher = form.save(commit=False)
         teacher.child = getuser   # link to user
         teacher.save()
         form.save_m2m()
         print("POST DATA:", request.POST)
         print("SUBJECT:", request.POST.get('subject'))
         usr = User.objects.get(id=request.user.id)
         context = {
              'usr' : teacher.child,
          }
         print(f" aa rahi id - {usr}")
         print(f" aa rahi id teacher - {teacher}")
         print(f" aa rahi id teacher - {teacher.child} FI {form.instance.child.id}")
         #print(form.errors)
         #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
         return render(request, "partials/usersrow.html", context)
       else:
          print(form.errors)
          print("FORM ERRORS ❌", form.errors)
    else:
        return render(request, "partials/teacherform.html", {'form' : form})


@login_required
def jobslist(request):
    print("Logged in user id:", request.user.id)
    #users = User.objects.filter(parent_id=request.user.id)
    #users = User.objects.all()
    joblist = Jobslist.objects.all()
    print(f"mere user hai {users}")
    #users = User.objects.filter(parent_id = request.user.id)
    context = {
     #   'users' : users,
        'joblist' : joblist
    }
    return render(request, "jobslist.html", context)

@login_required  
@vary_on_headers("HX-Request")
def addjob(request):
    if request.headers.get('HX-Request') and request.method == "GET":
       #form = AdduserForm(request.POST)
       form = JobpostForm()
       context = {
            'form' : form
        }
       return render(request, "partials/addjob.html", context)

@login_required  
@vary_on_headers("HX-Request")
def savejob(request):
    form = JobpostForm()
    if request.headers.get('HX-Request') and request.method == "POST":
        user = User.objects.get(id = request.user.id)
        form = JobpostForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.created_by = request.user
            user.save()
            #users = User.objects.filter(id=request.user.id).order_by('-id')
            context = {
                'job' : user,
            }
            #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
            return render(request, "partials/jobrow.html", context)
        else:
            response = render(request, "partials/adduser.html", {'form' : form} )
            response["HX-Retarget"] = "#adduser"
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = json.dumps({"failed": "Form me error hai"})
            #response['HX-Trigger-After-Settle'] = 'user_failed'
            return response 
    return render(request, "partials/adduser.html", {'form' : form})

@login_required  
@vary_on_headers("HX-Request")
def getjob(request, id):
    if request.headers.get('HX-Request') and request.method == "GET":
        jobobj = get_object_or_404(Jobslist, id=id)
        #tobj = get_object_or_404(Teacher, child=userobj)
        form = JobpostForm(instance = jobobj)   # ✅ FIX
        print(f"yah rahi id {id}")
        print(f"yah rahi form ins id {form.instance.id}")
        print(f"yah rahi form {form}")
        return render(request, "partials/jobform.html", {
            'form': form,
            'instance': jobobj      # 👈 IMPORTANT
        })

@login_required  
@vary_on_headers("HX-Request")
def savejob(request, id):
    print("SAVEJOB HIT")
    print(request.POST)
    print(id)
    getjob = get_object_or_404(Jobslist, id = id)       
    form = JobpostForm(instance=getjob)
    if request.headers.get('HX-Request') and request.method == "POST":
       getjob = get_object_or_404(Jobslist, id = id)       
       print(f"yah raha user {getjob}")
       #teacher, created = Jobslist.objects.get_or_create(created_by=getjob)
       form = JobpostForm(request.POST, request.FILES, instance=getjob)
       #form = TeacherForm(request.POST, request.FILES, instance = getuser)
       print(f"yah rahi id {getjob}")
       print(f"yah rahi id {form}")
       print("URL id:", id)
       print("Editing user:", getjob.id)
       print("Logged user:", request.user.id)
       if form.is_valid():
         teacher = form.save(commit=False)
         teacher.created_by = request.user
         teacher.save()
         print("POST DATA:", request.POST)
         job = Jobslist.objects.filter(created_by=request.user.id)
         context = {
              'job' : teacher,
          }
         print(f" aa rahi id - {job}")
         #print(form.errors)
         #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
         return render(request, "partials/jobrow.html", context)
       else:
          print(form.errors)
          print("FORM ERRORS ❌", form.errors)
    else:
        return render(request, "partials/jobform.html", {'form' : form})

@login_required  
#@vary_on_headers("HX-Request")
def schoolprofile(request):
    #print(User._meta.get_fields())
    getuser = User.objects.get(id=request.user.id)
    print(getuser)
    sprofilee = School.objects.get(created_by_id=5)
    print(sprofilee)
    print(request.user.id)
    context = {
      'sprofile' : sprofilee
    }
    return render(request, "schoolprofile.html", context )

@login_required  
@vary_on_headers("HX-Request")
def schooldetails(request):
        form = SchoolDetailsForm()   # ✅ FIX
        print(f"yah rahi id {id}")
        print(f"yah rahi form ins id {form.instance.id}")
        print(f"yah rahi form {form}")
        return render(request, "partials/schooldetails.html", {
            'form': form,
        })



@login_required  
@vary_on_headers("HX-Request")
def saveschool(request, id):
    if request.headers.get('HX-Request') and request.method == "POST":
       profile = School.objects.get(created_by = request.user.id)
       print(f"yah tahi school is {profile}")
       form = SchoolDetailsForm(request.POST, request.FILES, instance = profile)
       if form.is_valid():
          form.save()
          messages.success(request, "ok saved form")
          profile = School.objects.get(created_by = request.user.id)
          response = render(request, "partials/schoolprofile.html", {'profile' : profile })  
          response['HX-Trigger'] = json.dumps({'success' : "ok success" })
          response.write('<div id="schoolprofile" hx-swap-oob="true"></div>')
          return response
       else:
          form = ProfileForm(request.POST, instance=request.user)
          response = render(request, "partials/editprofile.html", {'form' : form} )
          response['HX-Retarget'] = '#editprofile'
          response['HX-Reswap'] = 'outerHTML'
          response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
          return response 
    form = ProfileForm(instance=request.user)
    return render(request, "partials/editprofile.html", {"form": form})

@login_required  
@vary_on_headers("HX-Request")
def getschoolprofile(request, id):
    print(id)
    profile = School.objects.get(created_by=request.user.id)
    if request.headers.get('HX-Request') and request.method == "GET":
       #profile = User.objects.get(id=request.user.id)
       print(f"here is profile{profile}")
       form = SchoolDetailsForm(instance = profile)
       context = {
        'form' : form
        }
       return render(request, "partials/editschool.html", context)
    return render(request, "userprofile.html", {'profile' : profile })

@login_required  
@vary_on_headers("HX-Request")
def editschool(request, id):
    print(id)
    if request.headers.get('HX-Request') and request.method == "POST":
       profile = School.objects.get(id = id)
       form = SchoolDetailsForm(request.POST, request.FILES, instance = profile)
       if form.is_valid():
          form.save()
          messages.success(request, "ok saved form")
          profile = School.objects.get(created_by=request.user.id)
          response = render(request, "partials/schoolprofile.html", {'profile' : profile })  
          response['HX-Trigger'] = json.dumps({'success' : "ok success" })
          response.write('<div id="editschool" hx-swap-oob="true"></div>')
          return response
       else:
          form = ProfileForm(request.POST, instance=request.user)
          response = render(request, "partials/editprofile.html", {'form' : form} )
          response['HX-Retarget'] = '#editprofile'
          response['HX-Reswap'] = 'outerHTML'
          response['HX-Trigger'] = json.dumps({"failed": " ojk डेटा सृजन में सेव हो गया!"})
          return response 
    form = ProfileForm(instance=request.user)
    return render(request, "partials/editprofile.html", {"form": form})


@login_required  
@vary_on_headers("HX-Request")
def getstudent(request, id):
    if request.headers.get('HX-Request') and request.method == "GET":
        print(f"yah jaa rahi id - {id}")
        userobj = get_object_or_404(User, id=id)
        print(f" yah userobj id {userobj}")
        #userobj = get_object_or_404(User, id=id)
        sobj = get_object_or_404(Student, child=userobj)
        print(f" yah raha student {sobj}")
        form = StudentForm(instance=sobj)
        #form = StudentForm(instance=userobj)
        print(f"yah rahi id {id}")
        print(f"yah rahi form ins id {form.instance.id}")
        print(f"yah rahi form {form}")
        return render(request, "partials/studentform.html", {
            'form': form,
            'instance': sobj      # 👈 IMPORTANT
        })


@login_required  
@vary_on_headers("HX-Request")
def savestudent(request, id):
    if request.headers.get('HX-Request') and request.method == "POST":
       getuser = get_object_or_404(User , id = id)       
       print(f"yah raha user {getuser}")
       student, created = Student.objects.get_or_create(child=getuser)
       form = StudentForm(request.POST, instance=student)
       #form = TeacherForm(request.POST, request.FILES, instance = getuser)
       print(f"yah rahi id {getuser}")
       print(f"yah rahi id {form}")
       print("URL id:", id)
       print("Editing user:", getuser.id)
       print("Logged user:", request.user.id)
       if form.is_valid():
         student = form.save(commit=False)
         student.child = getuser
         student.save()
         form.save_m2m()
         print("POST DATA:", request.POST)
         print("SUBJECT:", request.POST.get('subject'))
         usr = User.objects.get(id=request.user.id)
         context = {
              'usr' : student.child,
          }
         print(f" aa rahi id - {usr}")
         print(f" aa rahi id teacher - {student}")
         print(f" aa rahi id teacher - {student.child} FI {form.instance.child.id}")
         #print(form.errors)
         #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
         return render(request, "partials/usersrow.html", context)
       else:
          print(form.errors)
          print("FORM ERRORS ❌", form.errors)
    else:
        return render(request, "partials/teacherform.html", {'form' : form})



@login_required
def marks(request):
    print("Logged in user id:", request.user.id)
    marks = User.objects.filter(parent_id=request.user.id)
    #marks = SubjectMark.objects.filter(child_id=request.user.id)
    #users = User.objects.all()
    teacher = Teacher.objects.all()
    print(f"mere user hai {users}")
    #users = User.objects.filter(parent_id = request.user.id)
    context = {
        'marks' : marks,
    }
    return render(request, "marks.html", context)

@login_required  
@vary_on_headers("HX-Request")
def addmarks(request):
    if request.headers.get('HX-Request') and request.method == "GET":
       #form = AdduserForm(request.POST)
       form = SubjectMarksForm()
       form = context = {
            'form' : form
        }
       return render(request, "partials/addmarks.html", context)


@login_required  
@vary_on_headers("HX-Request")
def savemarks(request):
    form = SubjectMarksForm()
    if request.headers.get('HX-Request') and request.method == "POST":
        mark = SubjectMark.objects.filter(child_id = request.user.id)
        form = SubjectMarksForm(request.POST, request.FILES)
        if form.is_valid():
            mark = form.save(commit=False)
            mark.child = request.user
            #password = form.cleaned_data.get('password')
            #user.set_password(password)
            form.save()
            form.save_m2m()
            #marks = SubjectMark.objects.filter(child_id=request.user.id).order_by('-id')
            #marks = SubjectMark.objects.filter(child_id=request.user.id)
            #print(f"yah rahe mere marks{marks}")
            context = {
                'mark' : mark,
            }
            #return HttpResponse("<tr><td>HELLO</td><td>TEST</td></tr>")
            return render(request, "partials/marksrow.html", context)
        else:
            response = render(request, "partials/adduser.html", {'form' : form} )
            response["HX-Retarget"] = "#adduser"
            response['HX-Reswap'] = 'outerHTML'
            response['HX-Trigger-After-Settle'] = json.dumps({"failed": "Form me error hai"})
            #response['HX-Trigger-After-Settle'] = 'user_failed'
            return response 
    return render(request, "partials/adduser.html", {'form' : form})
