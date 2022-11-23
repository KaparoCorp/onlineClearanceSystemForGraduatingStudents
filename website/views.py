from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from .form import LoginForm, register , StudentForm, AdminClearance
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from .models import UserInfo, Student, ClearanceForm

# Create your views here.
def home (request):
    return render(request, "home.html", {})


def loginView(request):
    if request.method == "POST":
        owner = request.user
        form = LoginForm(request.POST or None)
        
        if form.is_valid():
            username = request.POST.get("username", '')
            password = request.POST.get('password', '')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                studentInfo = Student.objects.get(username=username)
                user_info = UserInfo(userInfo=request.user,student=studentInfo)
                user_info.save()
                return redirect('clearance')
            else:
                messages.error(request, ('username or password is invalid'))
                return render(request, "registration/login.html", {'form': form,})

    else:
        form = LoginForm()
    
    return render(request, "registration/login.html", {"form": form})

def registration(request):
    if request.method == 'POST':
        form = register(request.POST or None)

        if form.is_valid():
           email = request.POST.get("email", '')
           new = User.objects.filter(email=email)
           
           if new.count():  
                messages.error(request, ('The email {} already exists').format(email))
                return redirect('registration')
           else:
               form.save()
               return redirect('loginView')

    else:
        form = register()
    return render(request, "registration.html", {"form": form})

def clearance(request):
    user = request.user
    studentInfo = Student.objects.get(username=user.username)
    return render(request, "clearanceform.html", {"user": user, "student":studentInfo })

def adminPage(request):
    if request.method == 'POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('studentClearance')
    else:
        form = StudentForm()
    return render(request, "admin.html", {"form":form})

def studentClearance(request):
    if request.method == 'POST':
        form = AdminClearance(request.POST or None)

        if form.is_valid():

            form.save()
            return redirect('clearance')
    else:
        form = AdminClearance()
    
    
    return render(request, "adminClear.html", {"form":form})
