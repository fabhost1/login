from email import message
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def home(request):

    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')

def register1(request):

    if request.method == 'POST':
        
        username=request.POST.get('username')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'email alredy exsist')
                return render(request,'register.html')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'username alredy exsist')
                return render(request,'register.html')
            else:
                user=User.objects.create(first_name=firstname,last_name=lastname,username=username,email=email,password=password1)
                user.save()
                return render(request,'login.html')
        messages.info(request,'password dose not match ')
        return render(request,'register.html')

    else:
        return render(request,'register.html')

def login1(request):

    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username,password=password)
            value=request.POST.get('username')
            return render(request,'index1.html',{'value':value})
        except:
            messages.info(request,'username or password incorrect')
            return render(request,'login.html')
    else:
        return render(request,'login.html')
def logout(request):
    return render(request,'index.html')