from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include 
from .views import register , login_view, logout_view, profile_settings, userprofile, dashboard, invoice
from .views import editprofile, sample, users, usersdetails, adduser, saveuser, getteacher ,saveteacher, jobslist, addjob, getjob, savejob
from .views import schooldetails, schoolprofile, saveschool, getschoolprofile, editschool, getstudent, savestudent, marks, addmarks, savemarks

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
    path("getteacher/<int:id>/" , getteacher, name="getteacher"),
    path("saveteacher/<int:id>/" , saveteacher, name="saveteacher"),
    path("jobslist/", jobslist, name="jobslist"),
    path("addjob/" , addjob, name="addjob"),
    path("getjob/<int:id>/" , getjob, name="getjob"),
    path("savejob/<int:id>" , savejob, name="savejob"),
    path("schoolprofile/" , schoolprofile, name="schoolprofile"),
    path("schooldetails/" , schooldetails, name="schooldetails"),
    path("saveschool/<int:id>" , saveschool, name="saveschool"),
    path("editschool/<int:id>" , editschool, name="editschool"),
    path("getschoolprofile/<int:id>" , getschoolprofile, name="getschoolprofile"),
    path("getstudent/<int:id>/" , getstudent, name="getstudent"),
    path("savestudent/<int:id>/" , savestudent, name="savestudent"),
    path("marks/" , marks, name="marks"),
    path("addmarks/" , addmarks, name="addmarks"),
    path("savemarks/" , savemarks, name="savemarks"),
   
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)