from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django import forms
from .form import LoginForm, register , StudentForm, AdminClearance
from django.contrib.auth.forms import UserCreationForm 
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User , Group
from .models import UserInfo, Student, ClearanceForm, Hod, DeanOfSchool, University_library, UniversityAccommodationsSection,CateringSection, HealthUnit, GamesAndSportsOffice,DeanOfStudents, CentralServices, StudentsFinance, Registrar,FinanceOfficer 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import localdate
from django.core.mail import send_mail


# Create your views here.
@csrf_exempt
def home (request):
    return render(request, "home.html", {})

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
                return redirect('clearanceRegistration')
            else:
                messages.error(request, ('username or password is invalid'))
                return render(request, "registration/login.html", {'form': form,})

    else:
        form = LoginForm()
    
    return render(request, "registration/login.html", {"form": form})


@login_required
def clearanceRegistration(request):
    user = request.user
    if request.method == 'POST':
        form = StudentForm(request.POST or None)
        if form.is_valid():
            form.save()
            studentInfo = Student.objects.get(username=user.username)
            user_info = UserInfo(userInfo=user,student=studentInfo)
            user_info.save()
            return redirect('clearance')
    else:
        form = StudentForm()
    return render(request, "admin.html", {"form":form})

@login_required
def studentClearance(request):
    user=request.user
    if request.method == 'POST':
        form = AdminClearance(request.POST or None)
        

        if form.is_valid():
            student = request.POST.get("student", '')
            hod = request.POST.get("hod", '')
            dean_of_school = request.POST.get("dean_of_school", '')
            university_library = request.POST.get("university_library", '')
            university_accommodations_section = request.POST.get("university_accommodations_section", '')
            catering_section = request.POST.get("catering_section", '')
            health_unit = request.POST.get("health_unit", '')
            games_and_sports_office = request.POST.get("games_and_sports_office", '')
            dean_of_students = request.POST.get("dean_of_students", '')
            central_services = request.POST.get("central_services", '')
            student_finance = request.POST.get("student_finance", '')
            registrar = request.POST.get("registrar", '')
            finance_officer= request.POST.get("finance_officer", '')
            student_id = Student.objects.filter(registration_number=student)
        
            clearanceState = ClearanceForm(student=student_id[0],
                hod=hod,
                dean_of_school=dean_of_school,
                university_library=university_library,
                university_accommodations_section=university_accommodations_section,
                catering_section=catering_section,
                health_unit=health_unit,
                games_and_sports_office=games_and_sports_office,
                dean_of_students=dean_of_students,
                central_services=central_services,
                student_finance=student_finance,
                registrar= registrar,
                finance_officer=finance_officer,
                )
            clearanceState.save()

            return redirect('clearance')
    else:
        form = AdminClearance()
    
    
    return render(request, "adminClear.html", {"form":form, "user":user})


@login_required
def clearance(request):
    user = request.user
    studentInfo = Student.objects.get(username=user.username)
    print(studentInfo)
    clearanceformData = ClearanceForm.objects.get(student=studentInfo)
    return render(request, "clearanceform.html", {"user": user, "student":studentInfo, "clearanceformData":clearanceformData  })
