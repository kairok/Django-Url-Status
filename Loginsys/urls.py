from django.contrib import admin
#from django.urls import path
from django.conf.urls import include, url
from Loginsys import views

urlpatterns = [
    url(r'^login/', views.login, name='Login'),
    url(r'^logout/', views.logout, name='Logout'),
]
