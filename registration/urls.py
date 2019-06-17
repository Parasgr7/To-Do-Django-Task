from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from registration import views

urlpatterns = [
    url(r'^create/$', views.create, name='create'),
    url(r'^read/$', views.read, name='read'),
    url(r'^udpate_delete/$', views.update, name='update'),
    url(r'^save/$', views.save, name='save')

]