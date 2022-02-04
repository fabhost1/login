from pyexpat import model
from django.shortcuts import render
from django.contrib.auth.models import User  
from django.contrib import messages

# Create your views here.
def home(request):

    return render (request,'index.html')

def store(request):
    
    firstname=request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    email=request.POST.get('email')
    username=request.POST.get('username')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')
    if User.objects.filter(username=username).exists():
        messages.info(request,'user already exists')
        return render(request,'index.html')
    else:
        user=User.objects.create(username=username,first_name=firstname,last_name=lastname,email=email,password=password1)
        user.save
        return render(request,'base.html')
def login(request):
    return render(request,'login.html')
def login1(request):

    username=request.POST.get('username')
    password=request.POST.get('password')
    try:
        user=User.objects.get(username=username,password=password)
        messages.info(request,'login success')
        return render(request,'index.html')
    except:
        messages.info(request,'login faild')
        return render(request,'login.html')
