from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import CarForm
from .models import Car
from django.contrib.auth.decorators import login_required

# Create your views here.
def hview(request):

    return render(request,"car_app/home.html",{})

@login_required(login_url="/a2/lv/")
def carview(request):
    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"car_app/add_car.html",{"form":form})
@login_required(login_url="/a2/lv/")
def sview(request):
    car1 = Car.objects.all()
    print(car1)
    return render(request,"car_app/show.html",{"obj":car1})

def upview(request, pk):
    obj = Car.objects.get(cid=pk)
    form = CarForm(instance=obj)
    if request.method == "POST":
        form = CarForm(request.POST, instance=obj)

        if form.is_valid():
            form.save()
            return redirect("/a1/sv/")
    return render(request,"car_app/add_car.html",{"form":form})

def dview(request, x):

    ## confirm page ##
    obj = Car.objects.get(cid=x)
    if request.method == "POST":
        obj.delete()
        return redirect("/a1/sv/")
    return render(request,"car_app/success.html",{"obj":obj})