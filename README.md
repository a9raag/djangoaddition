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

## Description of project
* We are creating a sample web page for addition of two numbers using Django
* Django: Django is a free and open-source web framework, written in Python, which follows the **model-view-template** architectural pattern.
* The developer provides the Model, the view and the template then just maps it to a URL and Django does the magic to serve it to the user

![Basic Django Diagram](https://mdn.mozillademos.org/files/13931/basic-django.png)<br/>


### Flow of a Django project <br/>
![Basic Djang Flow Diagram](https://github.com/a9raag/djangoaddition/blob/plagiarism/Django-Template.png)
<br/>
## Addition  project



### Creating a Django Project<br/>
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
To start a web server you need to be in the project directory and run the following command <br/>
`anurag@anurag:~/addition$ python manage.py runserver 0.0.0.0:8000`
You will get the following message 
```
February 02, 2017 - 03:00:35
Django version 1.10.5, using settings 'sampleproject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Now all you need to do is check that your website is running. Open your browser (Firefox, Chrome, Safari, Internet Explorer or whatever you use) and enter this address:<br/>
[http://127.0.0.1:8000](http://127.0.0.1:8000)

##  Views <br/>
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template.
A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.
 In django views are created in `views.py` file.
 Here, we have defined a view `hello`
 In in function `hello(request)` we are additing two number 10 and 19  and rendering `hello.html` to display addition at
 "http://127.0.0.1:8000/hello" we will get to this part in Urls section
 ```python
 from django.shortcuts import render
 def hello(request):
    a = 10
    b = 19
    return render(request, "hello.html", {"result": a + b})
 ```
 
 ##   Templates<br/>
 All of your html files will be in `addition/template`.
 You need to create your own template directory by <br/>
 `anurag@anurag:~/addition$ mkdir template`
 ```
 addition 
├───manage.py
└───template
        hello.html
```
Now create a `hello.html` file template directory
 ```
 <html>

   <body>
      Hello World!!!<p>Addition of 10+19 is {{result}}</p>
   </body>

</html>
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

##  Urls
We want to access our view `hello` via a URL, first we need to associate that view with a URL. Django has his own way for URL mapping and it's done by editing your project url.py file (addition/url.py). 
First we need to import views `hello` from our views.py file
Which looks like this:<br/>
```python
from views import addition,hello
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', hello, name = 'hello'),
]
```
* Now that you have added a url for view `addition` you can access it at this url 
http://127.0.0.1:8000/hello
Restart the server using <br/>
`anurag@anurag:~/addition$ python manage.py runserver 0.0.0.0:8000`
`url(r'^', hello, name = 'hello')` This line means that for every URL that starts with hello/, Django will find a corresponding view.
## Models

* A model is a class that represents table or collection in our DB, and where every attribute of the class is a field of the table or collection. Models are defined in the app/models.py (in our example: addition/models.py)
```python
from django.db import models


class Numbers(models.Model):
    number1 = models.IntegerField()
    number2 = models.IntegerField()

    def __unicode__(self):
        return self.number1 + self.number2
```
Our class has 2 attribute `number1` and `number2` which are IntegerField, those will be the table fields.
### Creating forms using models
```python
class Numbers(forms.Form):
    class Meta:
        model = models.Numbers
        fields = ['number1', 'number2']

    number1 = forms.IntegerField()
    number2 = forms.IntegerField()
```
##	references links
[Django Urls](https://tutorial.djangogirls.org/en/django_urls/)
[Django Views](https://docs.djangoproject.com/en/1.10/intro/tutorial03/)
