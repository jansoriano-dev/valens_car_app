from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import *
from .forms import CarForm
from .filters import CarFilter

def car(request):
    cars = Car.objects.all()
    blueColor = cars.filter(color='Blue')
    redColor = cars.filter(color='Red')
    # myFilter = CarFilter(request.GET,queryset=car
    # cars = myFilter.qs
    context = {'cars':cars,'blueColor':blueColor,'redColor':redColor} 
    # context = {'cars':cars,'myFilter':myFilter}
    return render(request,'cars/index.html',context)

def createCar(request):

    form = CarForm()
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'cars/carorder.html',context)

def updateCar(request,pk):
    cars = Car.objects.get(id=pk)
    form = CarForm(instance=cars)
    if request.method == "POST":
        form = CarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'cars/carorder.html',context)

def deleteCar(request,pk):
    cars = Car.objects.get(id=pk)
    if request.method == 'POST':
        cars.delete()
        return redirect('/')
    context={'cars':cars}
    return render(request,'cars/delete.html',context)