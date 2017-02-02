# Addition Using Django
# PIP installation steps
* First, we need to install the pip package manager.
* pip is a package management system used to install and manage software packages written in Python.
* For python version 2.7.X use <br/>
`anurag@anurag:~$ sudo apt-get install python-pip`
* For python version 3.X use <br/>
`anurag@anurag:~$ sudo apt-get install python3-pip`
* Once you have installed pip, you are ready to install Django on your system.
## Django installation steps
* Pip will install the latest Django version available in pip repository
* Python 2.7.X   <br/>`sudo pip install django`
* Python 3.X     <br/>`sudo pip3 install django`
* You can verify Django installation by typing: <br/>
`anurag@anurag:~$ django-admin --version`

## description of project
* We are creating a sample web page for addition of two numbers using Django
* Django: Django is a free and open-source web framework, written in Python, which follows the **model-view-template** architectural pattern.
* The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the user
![Basic Django Flow](https://mdn.mozillademos.org/files/13931/basic-django.png)
    
### flow o project
<a href="https://github.com/a9raag/djangoaddition/blob/plagiarism/Django-Template.png"><img src="https://github.com/a9raag/djangoaddition/blob/plagiarism/Django-Template.png" align="left" height="512" width="512" ></a>
<br/>


## Addition  project
* Creating a sample django project named _addition_ we use following command


# Creating a Django Project
`anurag@anurag:~$ django-admin startproject addition`
This command will create directory named addition 
```
addition 
├───manage.py
└───addition
        settings.py
        urls.py
        wsgi.py
        __init__.py
```

* __init__.py − Just to make sure python handles this folder as a package.

* admin.py − This file helps you make the app modifiable in the admin interface.

* models.py − This is where all the application models are stored.


* views.py − This is where your application views are.


#  Starting a web server
To start a web server you need to be in the project directory and run the following command
`anurag@anurag:~/addition$ python manage.py runserver 0.0.0.0:8080`
You will get the following message 
```
February 02, 2017 - 03:00:35
Django version 1.10.5, using settings 'sampleproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Now all you need to do is check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:<br/>
[http://127.0.0.1:8000](http://127.0.0.1:8000)

##  views
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template.
A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.
 In django views are created in `views.py` file.
 ```python
 from django.shortcuts import render
 def hello(request):
    today = datetime.datetime.now().date()
    a = 10
    b = 19
    return render(request, "hello.html", {"today": a + b})
 ```
 ##   templates<br/>
 All of your html files will be in `template`.
 You need to create your own template directory by <br/>
 `anurag@anurag:~/addition$ mkdir template`
 ```
 addition 
├───manage.py
└───template
        hello.html
```
 Now we have to edit our `settings.py` file, so that python knows where all of our html files reside.<br/>
 In `settings.py`, search for  `TEMPLATES` which looks like this 
 
 ```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [''], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Change it to 
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['template'], # <- name of our template directory
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
 And our `hello.html` file looks like this 
 ```
 <html>

   <body>
      Hello World!!!<p>Today is {{today}}</p>
   </body>

</html>
```
##  urls
We want to access that view via a URL, first we need to associate that view with URL. Django has his own way for URL mapping and it's done by editing your project url.py file (addition/url.py). 
Which looks like this:<br/>
```python
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^add/', addition, name = 'add'), 
]
```
This line means that for every URL that starts with admin/, Django will find a corresponding view. In this case we're including a lot of admin URLs so it isn't all packed into this small file – it's more readable and cleaner.


##	references links
[Django Urls](https://tutorial.djangogirls.org/en/django_urls/)
[Django Views](https://docs.djangoproject.com/en/1.10/intro/tutorial03/)
