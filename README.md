# myfirstpyfolder
PythonDemo
INSTALLING PYTHON AND DJANGO

•	DOWNLOAD PYTHON AT https://www.python.org/downloads/
•	INSTALL PYTHON AND MAKE SURE YOU SELECT THE BOX  ‘ADD PYTHON TO PATH’
•	GO TO YOUR COMMAND LINE 
•	FROM THE CMD LINE TYPE : python --version
•	The version of the python installed would be displayed
•	FROM THE CMD LINE OR POWERSHELL TYPE : pip --version

STEPS IN PYTHON WEB APP DEVELOPMENT
You can simply used anaconda because with it there is no need for virtual environment. All you need to do is to go anaconda prompt and install Django

Steps
1.	Open your computer
2.	Go to the destination you want to the virtual environment to be domiciled in, preferably c:\Users\user
3.	Create folder called mypyfolder by typing at cmd prompt, 
c:\Users\user>mkdir mypyfolde 
Open command prompt and open the folder
4.	C:\Users\user>cd mypyfolder 
5.	Create a virtual environment with this command, c:\Users\user\mypyfolder>py -m venv env 
6.	Now activate the virtual environment, c:\Users\user\mypyfolder>.\\env\Scripts\activate 
Install django
7.	(env) c:\Users\user\mypyfolder>pip install django 
8.	(env) c:\Users\user\mypyfolder>Django-admin startproject myfirstproject
9.	Go to visual studio and open the folder myfirstproject
10.	Change to your app folder by typing (env) c:\Users\user\mypyfolder>cd myfirstproject
11.	To run server type, (env) c:\Users\user\mypyfolder\myfirstproject>python manage.py runserver
12.	Then open browser and type 127.0.0.1:8000 or localhost:8000
13.	Continue on app development, open the command prompt
14.	Repeat 4,and 5
15.	(env) c:\Users\user\mypyfolder\myfirstproject>python manage.py startapp myfirstapp

STEPS IN CONFIGURING YOUR DJANGO FRAMEWORK

In view, type this:

from Django.http import HttpResponse
def home(request):
	return HttpResponse(‘<h1>Home Blog </h1>’)

example2: add more pages to your site
in view type:
from Django.http import HttpResponse
def home(request):
	return HttpResponse(‘<h1>Home Blog </h1>’)

def about(request):
	return HttpResponse(‘<h1>About Blog </h1>’)



in project url, type this: 
from django.urls import path, include
urlpatterns = [path(‘blog/’, include(‘blog.urls’)),]

to add more pages, leave the first path with emty quote like below
urlpatterns = [path(‘ ’, include(‘blog.urls’)),
]
	

To create a good website or web app, we need to build templates
•	Go to your app folder let’s say social
•	Create a folder called templates
•	Inside the template folder, create another folder called social
•	Inside social folder, create home.html, about.html and as many pages as you want in your app
•	Develop the contents of the pages in the template
•	Then go to your app folder(here social), open app.py, copy the class called SocialConf
•	Open settings.py from project folder (here futo), go to the list called INSTALLED_APP as follows
INSTALLED_APPS = [
	‘social.apps.SocialConfig’,
		.
		.



another example
in app url, u created, type this:
from . import views
urlpatterns = [ path(‘ ’, views.home, name = ‘blog-home’),
	            path(‘ about’, views.about, name = ‘blog-about’),	
]




