from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Comment

def index(request):
    # TODO: Implement lists of comments? Potentially datatables-like filtering.
    return HttpResponse("Hello....")

def detail(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    context = { 'comment': comment }
    return render(request, 'comments/index.html', context)
