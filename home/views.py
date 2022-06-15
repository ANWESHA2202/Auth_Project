from distutils.log import log
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,'index.html')

def loginUser(request):
    
    if request.method=="POST":
        password = request.POST.get('password')
        username=request.POST.get('username')
        
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            print("login success")
            return render(request,'index.html')
        else:
            return render(request,'login.html',{'error':'Invalid Credentials'})
    return render(request,'login.html')

def logoutuser(request):
    logout(request)
    return redirect('/login')
