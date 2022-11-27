# Breakdown on how I made the ocs website using django
I prefer django but had initially started the project with flask .
I have choosen Sqlite as my database

## Creating virtual environment
I started by fist runing my virtual environment by running 
```
> python3 -m venv ocs
This set up a virtual environment and created a folder named "ocs"
>ocs
    >>include
    >>Lib
    >>Script
    >>pyvenv.cfg
```
After I activated the environment
>source ocs/bin/activate
After I activated the virtual environment
I saw
>(ocs) ...$ 
on the terminal window

## Installing Django
```
python3 -m pip install Django
```
This installed Django
To confirm installation after the script had run I tried to see the Django version installed by running
```
django-admin --version
```
It returned 4.0.3 and I had confirmed that Django had been installed successfully

## Creating project
After I had to create my project 
```
>django-admin startproject ocs
```
I called the filename of my project and environment the same for easier access of files 
This created a folder
>ocs
    >>manage.py
    >>ocs/
        >>__init__.py
        >>asgi.py
        >>settings.py
        >>urls.py
        >>wsig.py
        >>db.sqlite3
After I tried to run the server
>python3 manage.py runserver
The script run and I accessed the website at http://127.0.0.1:8000/

## Creating App
I will name my first app users
This will be the user login and registration authorisation section
I created the app
>python3 manage.py startapp users
This created a file users inside ocs with files
>users  
    >>migrations
    >>__init__.py
    >>admin.py
    >>models.py
    >>apps.py
    >>tests.py
    >>views.py

## Views in Django
Views is how Django handles http requests and returns http response, like Html
documents.
You change the views content by adding 
>from django.http import HTTpResponse
This imports HTTpResponse from django.http and this is what  helps in the html respose being posted 
The we add 
>def index(request):
    >return HTTpRestponse("Hello world!")
After I created a file named urls.py in the same folder as out views.py
And add 
>from django.urls import path
>from . import views
>urlpatterns = [path('', views.index, name='index'),]
This url.py is specific to the users application 
I had to do some routing to the root directory ocs as well 
I had to go to the urls.py file in the ocs directory and add the include as a module using an import statement and add path in urlpatterns list 
In the urlpatterns I added
>path('users/', include('users.urls')),
And at from django.urls import path I added include