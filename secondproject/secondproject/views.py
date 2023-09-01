from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from contact.models import Contact


def saveenquary(request):
    if request.method=="POST":
        name=request.POST.get('name')
        lastname=request.POST.get('lastname')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        join_date=request.POST.get('join_date')
        en=Contact(f_name=name,l_name=lastname,contact_nu=phone,email=email,join_date=join_date)
        en.save()
    return render(request,"index.html")

def homePage(request):
    contactdata=Contact.objects.all().order_by('f_name')
    data={

            'contactdata':contactdata,
            }
    return render(request,"savedata.html",data)
    
   