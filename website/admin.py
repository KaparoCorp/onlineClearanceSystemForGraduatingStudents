from django.contrib import admin
from .models import SchoolInfo, StudentInfo , DepartmentInfo, UserInfo, ScienceSchoolInfo, StudentPersonalInfo

# Register your models here.
admin.site.register(SchoolInfo)
admin.site.register(StudentInfo)
admin.site.register(DepartmentInfo)
admin.site.register(ScienceSchoolInfo)
admin.site.register(UserInfo)
admin.site.register(StudentPersonalInfo)