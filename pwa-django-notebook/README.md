## wild meet progressive web app

# icon of pwa ![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/icons8-wild-animals-sign-80.png)
# pwa installed in mobile device ![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/appinstalled.jpg)
# pwa fullscreen in mobile device  ![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/homemobile.PNG)

# i use this TUTO for my app https://medium.com/beginners-guide-to-mobile-web-development/convert-django-website-to-a-progressive-web-app-3536bc4f2862
# create my project with
$ django-admin startproject djangopwa
# create my app with
$  python manage.py startapp note


after write some function in view i create models for register data in bdd and i add my app note in setting.py in INSTALLED_APPS
# after add my app i create my bdd with command
$ python manage.py makemigrations note

$ python manage.py migrate

# for use image in my bdd i install pillow with command
$ pip install pillow

# i create super user with django admin with command
$ python manage.py createsuperuser

i register my name , email and my password

# write code view models forms url

#  Add service worker with install django pwa

$ pip install django-progressive-web-app

add 'pwa' in settings.py in INSTALLED_APP

![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/installedapps.png)

# add app 'pwa' in urls in root directory

path(‘’, include(‘pwa.urls’)),

![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/pwaurls.png)

# create file servicesworker.js in /static/js/

add this variable in setting.py PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'posts/static/js', 'serviceworker.js')

![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/psw.png)

# add balise meta in base.html for load pwa szervicesworker

{% load pwa %}

<head>
    ...
    {% progressive_web_app_meta %}
    ...
</head>

