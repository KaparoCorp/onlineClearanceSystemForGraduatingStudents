from django.db import models

# Create your models here.
class UserInfo(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class StudentInfo(models.Model):
    registrationNumber = models.CharField(max_length=20, unique=True)
    firstName = models.CharField(max_length=20)
    middleName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    academicYear = models.CharField(max_length=20)
    yearOfStudy = models.IntegerField()

class SchoolInfo(models.Model):
    school_id = models.IntegerField()
    school_name= models.CharField(max_length=20)

class DepartmentInfo(models.Model):
    department_id = models.CharField(max_length=20)
    school_id = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=600)

class ScienceSchoolInfo(models.Model):
    school_id = models.ForeignKey(SchoolInfo, on_delete=models.CASCADE)
    registationNumber = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)

class StudentPersonalInfo(models.Model):
    registration_number = models.ForeignKey(StudentInfo, on_delete=models.CASCADE)
    school = models.ForeignKey(SchoolInfo, on_delete=models.DO_NOTHING)
    department = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)
    year_of_study = models.CharField(max_length=20)