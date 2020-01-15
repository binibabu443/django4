from django.urls import path
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',TemplateView.as_view(template_name='login.html'),name='login'),
   
    path('stuleave/',TemplateView.as_view(template_name='student-leave.html'),name='student-leave'),
    path('assess/',TemplateView.as_view(template_name='assessment.html'),name='assessment'),
    path('attend/',TemplateView.as_view(template_name='attendence_1.html'),name='attendence_1'),
    path('profilefac/',TemplateView.as_view(template_name='faculty-profile.html'),name='faculty-profile'),
    path('forwardleave/',TemplateView.as_view(template_name='leave-forwarded.html'),name='leave-forwarded'),
    path('rejectedleave/',TemplateView.as_view(template_name='leave-rejected.html'),name='leave-rejected'),
    
    path('homestudent/',TemplateView.as_view(template_name='student-login.html'),name='student-login'),
    path('index',views.authentication,name='submit'),
    path('proview',views.facprofile,name='faculty-profile'),
    path('proviewdetails',views.facprofileview,name='faculty-profiles'),

    
    path('edit',views.facupdate,name='fac-profile-edit'),
    path('faclogin/',TemplateView.as_view(template_name='faculty-login.html'),name='faculty-login'),

    ]