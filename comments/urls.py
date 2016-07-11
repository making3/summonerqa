from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<comment_id>[0-9A-Za-z]+)/$', views.detail, name='detail')
]
