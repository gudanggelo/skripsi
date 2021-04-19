from django import urls
from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('download', views.download, name='download'),
    path('maps/', views.peta, name='maps'),
    path('login/',views.loginPage , name='login'),
    path('register/',views.registerPage, name='register'),
    path('logout/', views.logoutUser, name="logout"),
]
