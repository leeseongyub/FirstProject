from . import urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^home/comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^home/comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
