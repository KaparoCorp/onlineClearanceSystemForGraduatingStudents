from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Student(models.Model):

    schools=(
        ('Education','Education'),
        ('Arts, Social Science and Business','Arts, Social Science and Business'),
        ('Information Communication and Media Studies','Information Communication and Media Studies'),
        ('Science Agriculture and Environmental Studies','Science Agriculture and Environmental Studies')
    )

    registration_number = models.CharField(max_length=20, unique=True, primary_key=True)
    academic_year = models.CharField(max_length=20)
    school = models.CharField(max_length=50, choices=schools)
    year_of_study = models.IntegerField()
    username = models.CharField(max_length=20)
    department = models.CharField(max_length=20)

class UserInfo(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    userInfo = models.ForeignKey(User, on_delete=models.CASCADE)
    

class Hod(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class DeanOfSchool(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class University_library(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class UniversityAccommodationsSection(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class CateringSection(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class HealthUnit(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class GamesAndSportsOffice(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class DeanOfStudents(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class CentralServices(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class StudentsFinance(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class Registrar(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class FinanceOfficer(models.Model):
    is_cleared = models.BooleanField()
    costed_owed = models.IntegerField()
    date = models.DateField()
    name = models.CharField(max_length=15)

class ClearanceForm(models.Model):
    is_cleared = (
        ('cleared','cleared'),
        ('not cleared', 'not cleared')
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    hod = models.CharField(max_length=15, choices=is_cleared)
    dean_of_school = models.CharField(max_length=15, choices=is_cleared)
    university_library= models.CharField(max_length=15, choices=is_cleared)
    university_accommodations_section = models.CharField(max_length=15, choices=is_cleared)
    catering_section = models.CharField(max_length=15, choices=is_cleared)
    health_unit = models.CharField(max_length=15, choices=is_cleared)
    games_and_sports_office = models.CharField(max_length=15, choices=is_cleared)
    dean_of_students = models.CharField(max_length=15, choices=is_cleared)
    central_services = models.CharField(max_length=15, choices=is_cleared)
    student_finance = models.CharField(max_length=15, choices=is_cleared)
    registrar = models.CharField(max_length=15, choices=is_cleared)
    finance_officer = models.IntegerField()
   
    