from django.shortcuts import render
from django.shortcuts import HttpResponse 
from student.models import students
from django.http import HttpResponse
# Create your views here.


def authenticat(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=students.objects.filter(username=username,password=password)
        if u.count()==1:
            request.session['usernm']=username
            qry=students.objects.all().filter(username=username)[0]
            return render(request,'student-login.html')
        else:
           return HttpResponse('login unsuccesful')  


               

