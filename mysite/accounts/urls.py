from . import urls
from django.conf.urls import url
from . import views
from django.contrib.auth import views
from home.models import Post

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
]
