from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#index - main page of an app
def index(request):
    return HttpResponse('Hello World')
