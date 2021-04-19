from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse, Http404
import os
import json
import sentinelsat
import geojson
from sentinelsat.sentinel import SentinelAPI, read_geojson, geojson_to_wkt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from datetime import date, datetime, timedelta
from . import config
from .forms import OrderForm, CreateUserForm
from .models import *


#method view index
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def peta(request):
    return render(request,'maps.html')

#Creata and Login 
def registerPage(request):
    form =CreateUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user )
            
            return redirect('login')

    context ={'form':form}
    return render(request, 'register.html', context)

def loginPage(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None: 
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorret')

    context = {}
    return render(request,'login.html',context)

def logoutUser(request):
	logout(request)
	return redirect('maps')

def download(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        footprint = geojson_to_wkt(geojson.loads(data['geoJson']))
        username = config.username # ask ITC for the username and password
        password = config.password
        api = SentinelAPI(username, password, "https://scihub.copernicus.eu/apihub/") # fill with SMARTSeeds user and password
        tanggal = '[{0} TO {1}]'.format(data['dateFrom'].replace('.000Z', 'Z'), data['dateTo'].replace('.000Z', 'Z'))
        print (tanggal)
        products = api.query(footprint, 
                     producttype =config.producttype,
                     orbitdirection =config.orbitdirection,
                     platformname='Sentinel-1',
                     date=tanggal
                     )
        api.download_all(products)
        return HttpResponse(request.body)

def format_date(in_date):
    """Format date or datetime input or a YYYYMMDD string input to
    YYYY-MM-DDThh:mm:ssZ string format. In case you pass an
    """
    if type(in_date) == datetime or type(in_date) == date:
        return in_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    else:
        try:
            return datetime.strptime(in_date, '%Y%m%d').strftime('%Y-%m-%dT%H:%M:%SZ')
        except ValueError:
            return in_date