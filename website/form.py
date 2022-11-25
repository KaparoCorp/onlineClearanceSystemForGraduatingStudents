from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from .models import Student, ClearanceForm

class LoginForm(forms.Form):
    username = forms.CharField(label="USERNAME", max_length=20 )
    password = forms.CharField(label="PASSWORD", max_length=20, widget=forms.PasswordInput() )
    class Meta:
        model = User

class register(UserCreationForm):
    username = forms.CharField(label="USERNAME", max_length=20)
    email = forms.EmailField(label="EMAIL", max_length=150)
    

    def username_clean(self):  
        username = self.cleaned_data['username']  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
        
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  
        
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  

        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2 

    def clean_firstname(self):
        first_name = self.cleaned_data['firstname']
        return first_name

    def clean_lastname(self):
        last_name = self.cleaned_data['lastname']
        return last_name    
    
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['registration_number','username','year_of_study', 'academic_year', 'school', 'department']

class AdminClearance(forms.Form):
    is_cleared = (
        ('cleared','cleared'),
        ('not cleared', 'not cleared')
        )
     
    student = forms.CharField(max_length=20)
    hod = forms.ChoiceField(required=False, choices=is_cleared)
    dean_of_school = forms.ChoiceField(required=False, choices=is_cleared)
    university_library= forms.ChoiceField(required=False, choices=is_cleared)
    university_accommodations_section = forms.ChoiceField(required=False, choices=is_cleared)
    catering_section = forms.ChoiceField(required=False, choices=is_cleared)
    health_unit = forms.ChoiceField(required=False, choices=is_cleared)
    games_and_sports_office = forms.ChoiceField(required=False, choices=is_cleared)
    dean_of_students = forms.ChoiceField(required=False, choices=is_cleared)
    central_services = forms.ChoiceField(required=False, choices=is_cleared)
    student_finance = forms.ChoiceField(required=False, choices=is_cleared)
    registrar = forms.ChoiceField(required=False, choices=is_cleared)
    finance_officer = forms.IntegerField()
        
    

    class Meta:
        model = ClearanceForm
        fields= ['student','hod', 'dean_of_school', 'university_library', 'university_accommodations_section', 'catering_section', 'health_unit', 'games_and_sports_office', 'dean_of_students', 'central_services', 'student_finance', 'registrar', 'finance_officer'] 