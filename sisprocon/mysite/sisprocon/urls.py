from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.views import login, logout_then_login
from . import views

urlpatterns = [

    url(r'^$', views.autenticar, name='autenticar'),
    url(r'^login$', views.do_login, name='login'),
    url(r'^logout$', views.do_logout, name='logout'),


]