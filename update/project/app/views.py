from django.shortcuts import render
from .models import employee
# Create your views here.
def home(request):

    return render(request,'index.html')
def store(request):

    data=employee()

    data.name1 = request.POST.get('name1')
    data.name2 =request.POST.get('name2')
    data.save()
    show=employee.objects.all()
    return render(request,'base.html',{'show':show})

def delete(request,id):

    user=employee.objects.get(id=id)
    user.delete()
    show=employee.objects.all()
    return render(request,'base.html',{'show':show})
def edit(request,id):
    show=employee.objects.get(id=id)
    #show=employee.objects.all()
    return render(request,'edit.html',{'show':show})
def update(request,id):

    user=employee.objects.get(id=id)
    user.name1=request.POST.get('name1')
    user.name2=request.POST.get('name2')
    user.save()
    show=employee.objects.all()
    return render(request,'base.html',{'show':show})
