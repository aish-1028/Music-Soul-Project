from django.contrib import admin
from django.urls import path
from App.common import views
urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("about",views.about,name="about"),
    path("enroll",views.enroll,name="enroll"),
    path("contact",views.contact,name="contact"),
    path("team",views.team,name="team"),
    path("batch",views.batch,name="batch"),
]
