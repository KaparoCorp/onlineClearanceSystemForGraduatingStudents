from django.contrib import admin
from .models import Student, ClearanceForm, UserInfo

# Register your models here.
admin.site.register(Student)
admin.site.register(ClearanceForm)
admin.site.register(UserInfo)
