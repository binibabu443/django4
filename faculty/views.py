from django.shortcuts import render
from faculty.models import facultysignup
from django.http import HttpResponse
# Create your views here.


def authentication(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        username=str(username)
        password=str(password)
        u=facultysignup.objects.filter(username=username,password=password)
        if u.count()==1:
            request.session['usernm']=username
            qry=facultysignup.objects.all().filter(username=username)[0]
            return render(request,'faculty-login.html')
        else:
           return HttpResponse('login unsuccesful')  
def facprofile(request):
     queryset=facultysignup.objects.all().filter()
     return render(request,'faculty-profile.html',{'authors':queryset})
     
def facprofileview(request):
     querysett=facultysignup.objects.all().filter()
     return render(request,'faculty-profile-edit.html',{'authorss':querysett})


def facupdate(request):
    if request.method=='POST':
        username=request.POST.get('username')
        designation=request.POST.get('designation')
        joiningdate=request.POST.get('joiningdate')
        qualification=request.POST.get('qualification')
        gender=request.POST.get('gender')
        number=request.POST.get('number')
        email=request.POST.get('email')
        batch=request.POST.get('batch')
        blood=request.POST.get('blood')
        dob=request.POST.get('dob')
        password=request.POST.get('password')
        confirm=request.POST.get('confirm')
        facultysignup.objects.filter(username=request.session['usernm']).update(username=username,
        designation=designation,joiningdate=joiningdate,qualification=qualification,gender=gender,number=number,
        email=email,batch=batch,blood=blood,dob=dob,password=password)
    return render(request,'faculty-profile.html')