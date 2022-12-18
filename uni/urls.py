from django.contrib import admin
from django.urls import path
from uni import views

urlpatterns = [
    path("",views.index,name='index'),
    path("about",views.about, name='about'),
    path("goals",views.goals, name='goals'),
    path("contact",views.contact, name='contact'),
]