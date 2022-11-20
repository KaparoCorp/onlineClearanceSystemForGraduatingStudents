from django.urls import path

from . import views

urlpatterns = [
   path("", views.create, name="create"),
   path("home/", views.home, name='home'),
   path("registration/", views.registration , name="registration"),
   
]
