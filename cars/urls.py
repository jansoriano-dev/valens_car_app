from django.urls import path
from . import views

urlpatterns = [
    path('', views.car,name='home'), 
    path('createCar/', views.createCar,name='createCar'), 
    path('updateCar/<str:pk>/', views.updateCar,name='updateCar'), 
    path('deleteCar/<str:pk>/', views.deleteCar,name='deleteCar'), 
]
