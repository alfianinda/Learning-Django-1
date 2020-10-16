### basic steps ###

# https://docs.djangoproject.com/

# django install using pip
# pip3 install django==2.0.2

# django install virtual environment
# pip3 install virtualenv

# making virtualenv dir
# virtualenv dirname

# activate venv
# source myvenv/bin/activate
# or for windows:
# myvenv/Scripts/activate.bat

# >>> exit()

# django-admin help

# Creating a new project 
# django-admin startproject projectname 

# python manage.py help

# Add an app to a project 
# python manage.py startapp appname

# Starting the server 
# python manage.py runserver

# Creating migrations 
# python manage.py makemigrations

# Migrate the database 
# python manage.py migrate

# Creating a Super User for the admin panel 
# python manage.py createsuperuser

# Collecting static files into one folder 
# python manage.py collectstatic

# .gitignore
# open gitignore.io and type "django", then copy the codes

### App inside project ###

# create a blog models, ex:
    # title
    # pub_date
    # body
    # image
# add the blog app to the settings 
    # copy class name from apps.py
    # put inside 'installed_apps'
# create a migration
# migrate
# add to the admin