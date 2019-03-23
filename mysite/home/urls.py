from . import urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.post_list, name='index'),
    url(r'^home/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^home/new/$', views.post_new, name='post_new'),
    url(r'^home/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^home/drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^home/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^home/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
