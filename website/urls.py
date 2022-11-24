from django.urls import path

from . import views

urlpatterns = [
     path("", views.home, name="home"),
     path("login/", views.loginView , name="loginView"),
     path("registration/", views.registration, name="registration"),
     path("clearance/", views.clearance, name="clearance"),
     path("clearanceRegistration/", views.clearanceRegistration, name="clearanceRegistration"),
     path("adminPage", views.studentClearance, name="studentClearance")
]
