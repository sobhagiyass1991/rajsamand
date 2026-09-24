from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.vary import vary_on_headers
#from django.contrib.auth.models import User 
from django.contrib import messages
from django.http import HttpResponse, FileResponse
from django.db.models import Q 
from .forms import ProfileForm, ContactForm, PincodeForm
import calendar
import json
import io
from .models import Tehsil , Notification, Message, Contact, Pincode 
from utilities.models import UtilityCategory
from government.models import SchemeCategory,  Scheme
#from accounts.models import SrijanApp, SrijanModule
#from accounts.models import User
from django.contrib.auth import get_user_model
User = get_user_model() # यह अपने आप आपके 'accounts.User' को उठा लेगा
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa # यह है असली जादूगर
import os
from django.conf import settings

def indexx(request):
    users = User.objects.all()
    context = {
        'users' : users
    }
    return render(request, "indexx.html", context)

def link_callback(uri, rel):
    """
    यह फंक्शन URI (जैसे /static/logo.png) को 
    सिस्टम के असली पाथ (C:/srijan/static/logo.png) में बदलता है।
    """
    # अगर static या media फोल्डर का इस्तेमाल हो रहा है
    if uri.startswith(settings.STATIC_URL):
        uri_path = uri.replace(settings.STATIC_URL, "").replace('/', os.sep) # स्लैश को सिस्टम के हिसाब से बदलो
        path = os.path.join(settings.STATIC_ROOT, uri_path)
    elif uri.startswith(settings.MEDIA_URL):
        path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))
    else:
        return uri

    # चेक करें कि फाइल सच में वहां है या नहीं
    if not os.path.isfile(path):
        raise Exception(f'फाइल नहीं मिली: {path}')
    return path

def reportlab(request):
    # 1. अपनी थीम वाली HTML को रेंडर करो
    html_string = render_to_string("invoices.html")
    
    # 2. खाली बफर बनाओ
    buffer = io.BytesIO()
    
    # 3. HTML + CSS को सीधे PDF में बदलो (pisa machine)
    pisa_status = pisa.CreatePDF(html_string, dest=buffer, link_callback=link_callback)
    
    # 4. अगर कोई एरर नहीं है, तो फाइल भेज दो
    if pisa_status.err:
        return HttpResponse('<h1>PDF जनरेट करने में गड़बड़ हुई!</h1>')
        
    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

def testing(request):
    value = "<b>Joel</b> <button>is</button> a <span>slug</span>"
    html = strip_tags(value)
    context = {
        'html' : html
    }
    return render(request, "testing.html", context)


def home(request):
#    mytehsils = Tehsil.objects.all()
#    print("COUNT:", mytehsils.count())
     notifications = Notification.objects.all()
     schemecategory = SchemeCategory.objects.all()
     #apps = SrijanApp.objects.all()
     #modules = SrijanModule.objects.all()
     #services = LssemsService.objects.all()
     #print(f"here is {services.count}")
 
     return render(request, "home.html", {
#        'mytehsils': mytehsils,
        'notifications' : notifications,
        'schemecategory' : schemecategory,
        #'apps' : apps,
        #'modules' : modules,
        #'services' : services
        })

def events(request):
    year = 2026
    month = 1

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)
    # month_days = [[0,1,2,3,4,5,6], [...], ...]

    events = {
        5: {"title": "Exam", "color": "red"},
        12: {"title": "Holiday", "color": "green"},
    }

    context = {
        "month_days": month_days,
        "events": events,
        "month_name": calendar.month_name[month],
        "year": year,
    }

    return render(request, "events.html", context)

def admin(request):
    return render(request, "admin/")

def geography(request):
    return render(request, "geography.html")

def physiography(request):
    return render(request, "physiography.html")

def mines(request):
    return render(request, "mines.html")

def climate(request):
    return render(request, "climate.html")

def rivers(request):
    return render(request, "rivers.html")

def crops(request):
    return render(request, "crops.html")

def soils(request):
    return render(request, "soils.html")

def irrigation(request):
    return render(request, "irrigation.html")

def wildlife(request):
    return render(request, "wildlife.html")

def history(request):
    return render(request, "history.html")

def art_culture(request):
    return render(request, "art_culture.html")

def dances(request):
    return render(request, "dances.html")

def deity(request):
    return render(request, "deity.html")

def fairs(request):
    return render(request, "fairs.html")

def festivals(request):
    return render(request, "festivals.html")

def paintings(request):
    return render(request, "paintings.html")

def helpline(request):
    return render(request, "helpline.html")

def howtoreach(request):
    return render(request, "howtoreach.html")

def economy(request):
    return render(request, "economy.html")

def utilities(request):
    category = UtilityCategory.objects.all()
    context = {
        'category' : category
    }
    return render(request, "utilities.html", context)

def rural(request):
    return render(request, "rural.html")

def urban(request):
    return render(request, "urban.html")

def stateoffices(request):
    return render(request, "stateoffices.html")

def departments(request):
    return render(request, "departments.html")

def districtstructure(request):
    return render(request, "districtstructure.html")

def disadmin(request):
    return render(request, "disadmin.html")

def representatives(request):
    return render(request, "representatives.html")

def whoiswho(request):
    return render(request, "whoiswho.html")

def dprofile(request):
    return render(request, "dprofile.html")

def demography(request):
    return render(request, "demography.html")

def constituencies(request):
    return render(request, "constituencies.html")

def pureslider(request):
    return render(request, "pureslider.html")


def schemeview(request, id):
    g = SchemeCategory.objects.get(id=id)
    ischeme = Scheme.objects.filter(category=g).all()
    #scheme = Scheme.objects.get(slug=slug)

    return render(request, "schemeview.html", {
        'ischeme' : ischeme,
    }) 



def logout(request):
    auth_logout(request)
    return redirect('loginn')


def dashboard(request):

    return render(request, "dashboard.html")


def profile(request):
    profile_obj = SrijanProfile.objects.get(user=request.user)
    return render(request, "profile.html", {
        "profile" : profile_obj,
    })

def example(request):
    return render(request, "example.html")

def welcome(request):
    return render(request, "welcome.html")

def profile_settings(request):
    profile_obj = SrijanProfile.objects.get_or_create(user=request.user)
    return render(request, "profile_settings.html", {
        "profile": profile_obj,
    })

def sample_post(request):
    print("--- SERVER HIT SUCCESSFUL ---")
    import time 
    time.sleep(1)
    # 1. HTMX फ़िल्टर (Checkboxes) को सबसे पहले हैंडल करो
    if request.headers.get('HX-Request') and request.method == "GET":
        getx = request.GET.getlist('x')
        #getpc= request.GET.get('search_pincode').strip()
        getpc= request.GET.get('search_pincode')
        # अगर कोई चेकबॉक्स टिक है तो फ़िल्टर करो, वरना सब दिखाओ
        if getx:
            myresults = Pincode.objects.filter(circle__in=getx)
        elif getpc :
        # अगर कोई चेकबॉक्स टिक है तो फ़िल्टर करो, वरना सब दिखाओ
            myresults = Pincode.objects.filter(
                    Q(circle__icontains=getpc) | Q(office__icontains=getpc) | Q(pincode__icontains=getpc)
                )
        else:
             myresults = Pincode.objects.all().order_by('-id')

        return render(request, "partials/rows.html", { 'pincodelist' : myresults })

    
    # 2. POST (नया पिनकोड ऐड करना)
    if request.method == "POST":
        form = PincodeForm(request.POST)
        if form.is_valid():
            new_pin = form.save()
            response = render(request, "partials/rows.html", {'x': new_pin})
            response['HX-Trigger'] = 'success'
            return response
        else:
            return HttpResponse("", headers={'HX-Trigger': 'failed'})

    # 3. साधारण GET (पहली बार पेज लोड होने पर)
    pincodelist = Pincode.objects.all().order_by('-id')
    circles = Pincode.objects.values_list('circle', flat=True).distinct()
    form = PincodeForm()
    
    return render(request, "sample_post.html", { 
        'pincodelist' : pincodelist ,
        'form' : form,
        'circles' : circles
    })


def create_contact(request):
    pass
