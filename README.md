Project on CRUD Uisng Django


Steps to create project using Django

Step-1: **django-admin startproject <projectname> 
    This will create a mysite directory in your current directory

Step-2: Move to the project name directory and check for the presence of the following files
    mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
     
 Step-3: Verify the projectwork
       **python manage.py runserver   
       
Step-4: **python manage.py startapp <app name> i.e polls
Step-5: In the app directory create urls.py and add the below details
         from django.urls import path
         from . import views
         urlpatterns = [
             path('', views.index, name='index'),
         ]
step-6:Add the app url to the <project name> url i.e mysite urls.py
        from django.contrib import admin
        from django.urls import include, path
        urlpatterns = [
           path('polls/', include('polls.urls')),
           path('admin/', admin.site.urls),
           ]
step -7: create your first view in views.py
         from django.http import HttpResponse
        def index(request):
          return HttpResponse("Hello, world. You're at the polls index.")
