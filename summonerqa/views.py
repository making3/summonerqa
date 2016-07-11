from django.http import HttpResponse
from django.shortcuts import render

from tags.models import Tag

def index(request):
    tags = Tag.objects.values_list('name', flat=True)

    context = { 'tags': tags }
    return render(request, 'summonerqa/index.html', context)
