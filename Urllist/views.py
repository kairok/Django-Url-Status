from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import os
from django.conf import settings
from django.http import HttpResponse

from django.views.generic.detail import DetailView
from django.http import FileResponse
from django.http import Http404
# Create your views here.
from .models import Links
from datetime import datetime
#from pytz import timezone
from django.utils import timezone
from django.contrib import auth
import urllib.request
import requests


def index(request):

    if len(auth.get_user(request).username)==0:
        return render_to_response('index.html')
    clients = Links.objects.filter(creater=auth.get_user(request))
    check_status(clients)
    clients = Links.objects.filter(creater=auth.get_user(request))

    data = {"clients": clients, "username": auth.get_user(request)} #, "group":clientsgroup
    return render(request, "index.html", context=data)


def check_status(clients):
    #clients = Links.objects.filter(creater=auth.get_user(client))

    for userl in clients:
        URL = userl.url
        #response = urllib.request.urlopen(URL)
        try:
            response = requests.get(URL)
            print(response.status_code)
            status=response.status_code
        except:
            status=404

        updated_rows = Links.objects.filter(id=userl.id).update(status=status)


    return