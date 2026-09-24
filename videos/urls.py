from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import list, getadd, savenew, getedit, saveedit
#, include , ,  bookstatus, getaddstatus, savenewstatus, geteditstatus, saveeditstatus
app_name = 'videos'
urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path('list/', list, name='list'),   
    path("getadd/" , getadd, name="getadd"),
    path("savenew/" , savenew, name="savenew"),
    path("getedit/<int:id>/" , getedit, name="getedit"),
    path("saveedit/<int:id>/" , saveedit, name="saveedit"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)