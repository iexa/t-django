""" a minimalist django app - to be run as:
     django-admin runserver --pythonpath . --settings tiny

     https://simpleisbetterthancomplex.com/article/2017/08/07/a-minimal-django-application.html
        AND / OR
     https://github.com/rnevius/minimal-django/blob/master/minimal.py
"""     
from pathlib import Path
from django.http import HttpResponse
from django.urls import path
from django.shortcuts import render


BASE_DIR = Path(__file__).resolve().parent
DEBUG = True
# ALLOWED_HOSTS = ['*']
SECRET_KEY = 'gsgfdsfhgt4w534qfes@!#T&^FGF'
ROOT_URLCONF = __name__
TEMPLATES = [{
  "BACKEND": "django.template.backends.django.DjangoTemplates",
  "DIRS":[BASE_DIR],
  }]


def home(req):
  n = req.GET.get('n', 'nope')
  return HttpResponse(f"Hi there {n}!", content_type='application/json')


def about(req):
  return render(req, 'about.html', {'dogname': 'Yorkiez'})


urlpatterns = [
  path('', home),
  path('about', about)
]