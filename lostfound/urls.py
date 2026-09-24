from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from .views import itemlist, getaddform, saveadd, testing, getedit, saveeditlostfound
app_name = 'lostfound'

urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path("itemlist/" , itemlist, name="itemlist"),
    path("getaddform/" , getaddform, name="getaddform"),
    path("saveadd/" , saveadd, name="saveadd"),
    path("testing/" , testing, name="testing"),
    path("getedit/<int:id>/" , getedit, name="getedit"),
    path("saveeditlostfound/<int:id>/" , saveeditlostfound, name="saveeditlostfound"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)