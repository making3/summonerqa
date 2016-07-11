from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<thread_id>[0-9A-Za-z]+)/$', views.comments, name='comments')
]
