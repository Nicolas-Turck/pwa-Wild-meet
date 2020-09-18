## wild meet progressive web app

# icon of pwa ![alt text](https://raw.githubusercontent.com/Nicolas-Turck/pwa-django-notebook/master/djangopwa/note/static/images/icons8-wild-animals-sign-80.png)



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
