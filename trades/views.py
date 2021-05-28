from django.http import HttpResponse
from django.shortcuts import render
from .models import Trade

# Create your views here.

# index - main page of an app


def index(request):
    trades = Trade.objects.all()
    return render(request, 'trades/index.html', {'trades': trades})
