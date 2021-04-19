from django import urls
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='main-view'),
    path('download', views.download, name='download'),
    path('maps/', views.peta),
]
