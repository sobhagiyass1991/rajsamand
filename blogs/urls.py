from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#, include 
from .views import list, getadd, savenewblog, getedit, saveedit

app_name = 'blogs'

urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    #path('getautility/<int:id>/', getautility, name='getautility'),
    path('list/', list, name='list'),   
    path("getadd/" , getadd, name="getadd"),
    path("savenewblog/" , savenewblog, name="savenewblog"),
    path("getedit/<int:id>/" , getedit, name="getedit"),
    path("saveedit/<int:id>/" , saveedit, name="saveedit"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)