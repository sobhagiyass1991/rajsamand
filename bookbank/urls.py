from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#, include 
from .views import list, getedit, saveedit, getadd, savenew, bookstatus, getaddstatus, savenewstatus, geteditstatus, saveeditstatus
app_name = 'bookbank'
urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path('list/', list, name='list'),   
    path("savenew/" , savenew, name="savenew"),
    path("getadd/" , getadd, name="getadd"),
    path("getedit/<int:id>/" , getedit, name="getedit"),
    path("saveedit/<int:id>/" , saveedit, name="saveedit"),
    path("bookstatus/" , bookstatus, name="bookstatus"),    
    path("getaddstatus/" , getaddstatus, name="getaddstatus"),
    path("savenewstatus/" , savenewstatus, name="savenewstatus"),
    path("geteditstatus/<int:id>/" , geteditstatus, name="geteditstatus"),
    path("saveeditstatus/<int:id>/" , saveeditstatus, name="saveeditstatus"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)