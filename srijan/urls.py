from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include 
from main.views import home # या जहाँ भी आपका home फंक्शन है
#, search_venues
#schemeread

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('main/', include('main.urls', namespace='main')),
    path("" ,home, name="home"),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)