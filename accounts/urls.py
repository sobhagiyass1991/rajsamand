from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from .views import register , login_view, logout_view, profile_settings, userprofile, dashboard, invoice
from .views import editprofile, sample, users, usersdetails, adduser, saveuser

app_name = 'accounts'

urlpatterns = [
    #path('accounts/', include('accounts.urls')),
    #path('', home, name='home'),
    path('register', register, name='register'),
    path('login', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("profile_settings/" , profile_settings, name="profile_settings"),
    path("userprofile/" , userprofile, name="userprofile"),
    path('editprofile/', editprofile, name="editprofile"),
    path("dashboard/" , dashboard, name="dashboard"),
    path("invoice/" , invoice, name="invoice"),
    path("sample/" , sample, name="sample"),
    path("users/" , users, name="users"),
    path("usersdetails/<int:id>/" , usersdetails, name="usersdetails"),
    path("adduser/" , adduser, name="adduser"),
    path("saveuser/" , saveuser, name="saveuser"),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)