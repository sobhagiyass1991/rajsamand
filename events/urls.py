from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
#, include 
from .views import venues

app_name = 'events'

urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path('venues/', venues, name='venues'),
    #path('getautility/<int:id>/', getautility, name='getautility'),
    #path("saveteacher/<int:id>/" , saveteacher, name="saveteacher"),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)