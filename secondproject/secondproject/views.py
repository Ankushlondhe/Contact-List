from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from contact.models import Contact



def homePage(request):
    
    return render(request,"index.html")

def saveenquary(request):
    if request.method=="POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        en=Contact(f_name=name,l_name=lastname,contact_nu=phone,email=email)
        en.save()
    return render(request,"index.html")