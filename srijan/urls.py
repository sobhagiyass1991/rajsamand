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
    path('blood/', include('blood.urls', namespace='blood')),
    path('utilities/', include('utilities.urls', namespace='utilities')),
    path('lostfound/', include('lostfound.urls', namespace='lostfound')),
    path('mydjango/', include('mydjango.urls', namespace='mydjango')),
    path('events/', include('events.urls', namespace='events')),
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path("" ,home, name="home"),
    path('summernote/', include('django_summernote.urls')),
    path('bookbank/', include('bookbank.urls', namespace='bookbank')),
    path('videos/', include('videos.urls', namespace='videos')),
    path('news/', include('news.urls', namespace='news')),
    path('localservices/', include('localservices.urls', namespace='localservices')),
    path('estates/', include('estates.urls', namespace='estates')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)