from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from .views import donors, getadd, savedonor, getedit, saveedit, delete, donations, getadddonation,  getbloodgroup, comment, savedonation
from .views import saveeditdonation, geteditdonation, saveeditdonation, requests, geteditrequests, saveeditrequests, getbloodgroupvolume
from .views import getaddrequest
app_name = 'blood'

urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path("donors/" , donors, name="donors"),
    path("comment/" , comment, name="comment"),
    path("getadd/" , getadd, name="getadd"),
    path("savedonor/" , savedonor, name="savedonor"),
    path("getedit/<int:id>/" , getedit, name="getedit"),
    path("saveedit/<int:id>/" , saveedit, name="saveedit"),
    path("delete/<int:id>/" , delete, name="delete"),
    path("donations/" , donations, name="donations"),
    path("getadddonation/" , getadddonation, name="getadddonation"),
    path("getbloodgroup/" , getbloodgroup, name="getbloodgroup"),
    #path("getbloodgroup/<int:donorname>/" , getbloodgroup, name="getbloodgroup"),
    path("savedonation" , savedonation, name="savedonation"),
    path("saveeditdonation" , saveeditdonation, name="saveeditdonation"),
    path("geteditdonation/<int:id>/" , geteditdonation, name="geteditdonation"),
    path("saveeditdonation/<int:id>/" , saveeditdonation, name="saveeditdonation"),
    path("requests/" , requests, name="requests"),
    path("geteditrequests/<int:id>/" , geteditrequests, name="geteditrequests"),
    path("saveeditrequests/<int:id>/" , saveeditrequests, name="saveeditrequests"),
    path("getbloodgroupvolume/" , getbloodgroupvolume, name="getbloodgroupvolume"),
    path("getaddrequest/" , getaddrequest, name="getaddrequest"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)