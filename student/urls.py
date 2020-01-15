from django.urls import path
from student import views
from django.views.generic import TemplateView
urlpatterns = [
    path('studentlogin',TemplateView.as_view(template_name='home.html'),name='student/home'),
    path('studentattend',TemplateView.as_view(template_name='student-attendence.html'),name='student-attendence'),
    path('studentassess',TemplateView.as_view(template_name='student-assessment.html'),name='student-assessment'),
    path('studentleave',TemplateView.as_view(template_name='student-leave-management.html'),name='student-leave-management'),
    path('studentleaveapplied',TemplateView.as_view(template_name='student-applied-leave.html'),name='student-applied-leave'),
    path('studentprofile',TemplateView.as_view(template_name='student-profile.html'),name='student-profile'),
    path('profileedit',TemplateView.as_view(template_name='student-edit.html'),name='student-edit'),


     path('stdlogin',TemplateView.as_view(template_name='student-login.html'),name='student-login'),
     path('stdlogin',views.authenticat,name='stud-submit'),
]
