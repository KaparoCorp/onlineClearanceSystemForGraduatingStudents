from django.contrib import messages
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import CreateNew, RegistrationForm
from .models import DepartmentInfo, SchoolInfo, StudentInfo, UserInfo

# Create your views here.

def create(request):
    if request.method == "POST":
        form = CreateNew(request.POST)
        
        if form.is_valid(): 
            # user_name = form.cleaned_data["username"]
            # password = form.cleaned_data["password"]
             form.save()

    else:
        form = CreateNew()

    return render(request, "create.html", {"form": form})

def registration(response):
    if response.method == "GET":
        form = RegistrationForm(response.GET)

        if form.is_valid():
            registrationNumber = form.cleaned_data["registration_number"]
            school = form.cleaned_data["school"]
            department = form.cleaned_data["department"]
            academicYear = form.cleaned_data["academic_year"]
            yearOfStudy = form.cleaned_data["year_of_study"]



            return render(response, "fee.html", {})


        
    else:
        form = RegistrationForm()
   
    return render(response, "registration.html", {"form": form})



def home(response):
    return render(response, "home.html", {})

