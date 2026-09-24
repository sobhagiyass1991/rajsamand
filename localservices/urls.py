from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 
from .views import lssems, lssemsedit
#lssemsindex, 
app_name = 'localservices'
urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', home, name='home'),
    #path('lssemsindex/', lssemsindex, name='lssemsindex'),
    path('lssems/', lssems, name='lssems'),
    path('lssemsedit/<int:id>/', lssemsedit, name='lssemsedit'),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)