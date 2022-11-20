from django import forms
from .models import UserInfo, StudentPersonalInfo


choice = (
    ("1", "Education"),
    ("2","Science Agriculture and Environmental Studies" ) ,
    ("3","Information and communication" ),
    ("4" , "arts"),
)

class CreateNew(forms.Form):
    username = forms.CharField(label="USERNAME", max_length=200)
    password = forms.CharField(label="PASSWORD", max_length=200)

    def clean_message(self):
        user_name = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = UserInfo.objects.filter(userName = user_name)
        if not user:
            raise forms.ValidationError("Wrong username / password")
        return user_name , password


   

class RegistrationForm(forms.Form):
    registration_number = forms.CharField(label="REGISTRATION NUMBER", max_length=200)
    school = forms.ChoiceField(label="School", choices=choice )
    department = forms.CharField(label="Department", max_length=100)
    academic_year = forms.CharField(label="Academic Year", max_length=15)
    year_of_study= forms.IntegerField(label="Year of Study", max_value=4)

   
    class Meta:
        model = StudentPersonalInfo
        fields=["Registration_number", "school", "department", "academic_year" "year_of_study"]
