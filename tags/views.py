from django.http import HttpResponse
from django.shortcuts import render

from .models import Tag

def index(request):
    return render(request, 'tags/index.html')
