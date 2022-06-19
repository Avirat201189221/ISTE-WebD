from django.shortcuts import render, HttpResponse , redirect
from Home.models import Login
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
# Create your views here.
#test user is person1 with password: person1kapassword
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
            return redirect("/")
            
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return render(request,"login.html")

    