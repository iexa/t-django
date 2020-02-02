from django.shortcuts import render
from django.http import HttpResponse


def homePageView(req):
  return HttpResponse("Hello Gecc!")
