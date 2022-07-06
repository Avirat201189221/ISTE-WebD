from django.shortcuts import render, HttpResponse , redirect
from Home.models import Login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# Create your views here.
#test user is person1 with password: person1kapassword
#test faculty is faculty1.faculty password: iamafacultyperson
#test student is student1.student password: iamastudentperson
def index(request):
    if (request.user.is_anonymous):
        return redirect("/login")
    return render (request, "index.html")

def login(request):
    if request.method=="POST":
        email=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            messages.success(request, 'Login complete')
            if ".faculty" in email:
                return redirect("/faculty")
            elif ".student" in email:    
                return redirect("/")
            
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect("/login")

def facultyPage(request):
    return render(request,"facultyIndex.html")

def profilePage(request):
    return render(request,"profile.html")

def myHerupaFirstYear(request):
    return render(request,"myherupa-first-year.html")

def myHerupaSecondYear(request):
    return render(request,"myherupa-second-year.html")

def myHerupaThirdYear(request):
    return render(request,"myherupa-third-year.html")

def newsrs(request):
    return render(request, "Webkiosk/newSRS.html")