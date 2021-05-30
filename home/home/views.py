from django.shortcuts import render
from home.models import *
from django.contrib import messages
from home.models import order
# from home.form import form
# Create your views here.
def aboutus(request):
    return render(request,'aboutus.html')


def home(request):
    return render(request,'home.html')

def services(request):
    cats=catogary.objects.all()
    image=images.objects.all()

    data={
       'image':image,
       'cats':cats

    }
    return render(request,'services.html',data)

def show_catogary(request,cid):
    cats=catogary.objects.all()

    cato=catogary.objects.get(pk=cid)
    print(cato)
    image=images.objects.filter(cat=cato)

    data={
       'image':image,
       'cats':cats
    }

    return render(request,'showcat.html',data)



def reciveorder(request):

    return render(request,'order.html')

def placeorder(request):
    if request.method=='POST':

        print("mekoorder klaa")
        form=order()
        form.name=request.POST.get('name')
        form.catogary=request.POST.get('cat')
        form.itemcode=request.POST.get('itemcode')
        form.city=request.POST.get('city')
        form.state=request.POST.get('state')
        form.zip=request.POST.get('zipcode')

    
        form.save()

        messages.success(request,"nwe order recived "+form.name+"!!")

    return render(request,'home.html')

