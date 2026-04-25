from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 
from .views import home, geography, physiography, mines, climate, rivers, crops, soils, irrigation, wildlife, history, art_culture,  dances
from .views import deity, fairs ,festivals, paintings , helpline, howtoreach, economy, utilities, rural, urban , stateoffices, departments
from .views import representatives, whoiswho, dprofile, demography, constituencies,  events, districtstructure, disadmin, pureslider 
#from .views import pandas, logout, dashboard, profile, profile_settings, sample_post, example, schemeview
#from .views import contacts, search_contacts, create_contact, edit_contact, delete_contact, welcome , venues
from .views import lssemsindex, lssems, lssemsedit, reportlab, testing, indexx
#, lssemsservices

app_name = 'main'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('geography/', geography, name='geography'),
    path('lssemsindex/', lssemsindex, name='lssemsindex'),
    path('lssems/', lssems, name='lssems'),
    path('lssemsedit/<int:id>/', lssemsedit, name='lssemsedit'),
    path('reportlab/', reportlab, name='reportlab'),
    path('physiography/', physiography, name='physiography'),
    path('testing/', testing, name='testing'),
    path('mines/', mines, name='mines'),
    path('climate/', climate, name='climate'),
    path('rivers/', rivers, name='rivers'),
    path('crops/', crops, name='crops'),
    path('soils/', soils, name='soils'),
    path('irrigation/', irrigation, name='irrigation'),
    path('wildlife/', wildlife, name='wildlife'),
    path('history/', history, name='history'),
    path('art_culture/', art_culture, name='art_culture'),
    path('dances/', dances, name='dances'),
    path('deity/', deity, name='deity'),
    path('fairs/', fairs, name='fairs'),
    path('festivals/', festivals, name='festivals'),
    path('paintings/', paintings, name='paintings'),
    path("helpline/" ,helpline , name="helpline"),
    path("howtoreach/" ,howtoreach , name="howtoreach"),
    path("economy/" ,economy , name="economy"),
    path("utilities/" ,utilities , name="utilities"),
    path("rural/" ,rural , name="rural"),
    path("urban/" ,urban , name="urban"),
    path("stateoffices/" ,stateoffices , name="stateoffices"),
    path("departments/" ,departments , name="departments"),
    path("districtstructure/" ,districtstructure , name="districtstructure"),
    path("disadmin/" ,disadmin , name="disadmin"),
    path("representatives/" ,representatives , name="representatives"),
    path("whoiswho/" ,whoiswho , name="whoiswho"),
    path("dprofile/" ,dprofile , name="dprofile"),
    path("demography/" ,demography , name="demography"),
    path("constituencies/" ,constituencies , name="constituencies"),
    path("events/" ,events , name="events"),
    path("pureslider/" , pureslider, name="pureslider"),
    path("indexx/" , indexx, name="indexx"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)