# Addition Using Django
##	django installation steps
* Installing pip globally on Ubuntu 
* Django Installation using PIP
* pip is a package management system used to install and manage software packages written in Python.
* For python version 2.7.X use
`sudo apt-get install python-pip`
* For python version 3.X use
`sudo apt-get install python3-pip`
* Once you have installed pip on your system you are ready to install Django on your system.
* Pip will install the latest version available in pip repository
* Python 2.7.X   `sudo pip install django`
* Python 3.X     `sudo pip3 install django`
* You can verify Django installation by typing:
`django-admin --version`
* Creating a sample django project named _addition_ we use following command
`django-admin startproject addition`
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

##  views
A view is a “type” of Web page in your Django application that generally serves a specific function and has a specific template.
A view function, or “view” for short, is simply a Python function that takes a web request and returns a web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, etc. Example: You use view to create web pages, note that you need to associate a view to a URL to see it as a web page.
 In django views are created in `views.py` file.
##  urls
We want to access that view via a URL. Django has his own way for URL mapping and it's done by editing your project url.py file (myproject/url.py). 
## 	addition  project
    - Create a new project in Django
##	description of project
    - In this project we are creating a sample web page for addition of two numbers
    - It will have a 
##	flow of project
![Django Flow] (https://github.com/a9raag/djangoaddition/blob/plagiarism/Django-Template.png)
![Basic Django Flow](https://mdn.mozillademos.org/files/13931/basic-django.png)
##	references links
