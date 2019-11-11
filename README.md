# **My Blog Code Documentation**

<b>Author:Odirichukwu J.C. <chiomajaco6@gmail.com>
___
###INSTALLING PYTHON AND DJANGO

___
1.DOWNLOAD PYTHON AT [python Download](https://www.python.org/downloads/ "The latest python download").   
2.INSTALL PYTHON AND MAKE SURE YOU SELECT THE BOX  
ADD PYTHON TO PATH  
3.GO TO YOUR COMMAND LINE  
4.FROM THE CMD LINE TYPE : python --version  
5.The version of the python installed would be displayed  
6.FROM THE CMD LINE OR POWERSHELL TYPE : pip --version
___
###STEPS IN PYTHON WEB APP DEVELOPMENT
___
<p align="justify">
You can simply used anaconda because with it there is no need for virtual environment. All you need to do is to go anaconda prompt and install Django
</p>

###Steps
<p align="justify">
1.	Open your computer<br>2.	Go to the destination you want to the virtual environment to be domiciled in, preferably c:\Users\user<br>
3.	Create folder called mypyfolder by typing at cmd prompt, 
c:\Users\user>mkdir mypyfolde or you just goto Users/user and create a folder
Open command prompt and open the folder<br>
4.	C:\Users\user>cd mypyfolder<br> 
5.	Create a virtual environment with this command, c:\Users\user\mypyfolder>py -m venv env <br>
6.	Now activate the virtual environment, c:\Users\user\mypyfolder>.\\env\Scripts\activate 
Install django<br>
7.	(env) c:\Users\user\mypyfolder>pip install django<br> 
8.	(env) c:\Users\user\mypyfolder>Django-admin startproject myfirstproject<br>
9.	Go to visual studio and open the folder myfirstproject<br>
10.	Change to your app folder by typing (env) c:\Users\user\mypyfolder>cd myfirstproject<br>
11.	To run server type, (env) c:\Users\user\mypyfolder\myfirstproject>python manage.py runserver<br>
12.	Then open browser and type 127.0.0.1:8000 or localhost:8000<br>
13.	Continue on app development, open the command prompt
14.	Repeat 4,and 5<br>
15.	(env) c:\Users\user\mypyfolder\myfirstproject>python manage.py startapp myfirstapp<br>
</p>

***
### STEPS IN CONFIGURING YOUR DJANGO FRAMEWORK
***
>
>#**In view, type this:**
>
    from Django.http import HttpResponse
    def home(request):
	    return HttpResponse('<h1>Home Blog </h1>')
>
    from django.http import HttpResponse
    def home(request):
         return HttpResponse('<h1>Home Blog </h1>)
	def about(request):    
	    return HttpResponse('<h1>About Blog </h1>')
>in project url, type this: 
>      
    from django.urls import path, include  
    urlpatterns = [path('blog/', include(�blog.urls�)),]


>to add more pages, leave the first path with emty quote like below:  
>
urlpatterns = [path(' ', include('blog.urls')),
]  

	
___
##To create a good website or web app, we need to build templates
___
1.	Go to your app folder lets say social
2.	Create a folder called templates
3.	Inside the template folder, create another folder called social
4.	Inside social folder, create home.html, about.html and as many pages as   you want in your app
5.Develop the contents of the pages in the template
6.	Then go to your app folder(here social), open app.py, copy the class called SocialConf
7.	Open settings.py from project folder (here futo), go to the list called   INSTALLED_APP as follows  
>
	INSTALLED_APPS = [  
		social.apps.SocialConfig',
		.
		.



###Another example  
***in app url, u created, type this:***
>  
	from . import views  
		urlpatterns = [ path(' ., views.home, name = 'blog-home'),  
		path(' about', views.about, name = 'blog-about'),	
]



