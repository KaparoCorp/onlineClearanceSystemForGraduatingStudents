from django.urls import path

from . import views

urlpatterns = [
     path("", views.home, name="home"),
     path("login/", views.loginView , name="loginView"),
     path("registration/", views.registration, name="registration"),
     path("clearance/", views.clearance, name="clearance"),
     path("adminPage/", views.adminPage, name="adminPage"),
     path("adminPage/clearance/", views.studentClearance, name="studentClearance")
]
