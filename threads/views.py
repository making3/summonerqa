from django.http import HttpResponse
from django.shortcuts import render

from comments.models import Comment

def index(request):
    # TODO: Implement list of threads (possible datatables filtering again).
    return HttpResponse("Hello....")

def comments(request, thread_id):
    comments = Comment.objects.filter(thread=thread_id)
    context = { 'comments': comments }
    return render(request, 'threads/index.html', context)
