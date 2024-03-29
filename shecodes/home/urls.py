from django.contrib import admin
from django.urls import path, include
from home import views

admin.site.site_header = "sheCodes Admin"
admin.site.site_title = "sheCodes Admin Panel"
admin.site.index_title = "Welcome to sheCodes Admin Panel"

urlpatterns = [
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('about', views.about, name="about"),
    path('search', views.search, name="search"),
    path('search', views.search, name="search"),
    path('signup', views.handleSignUp, name="handleSignUp"),
    path('login', views.handeLogin, name="handleLogin"),
    path('logout', views.handelLogout, name="handleLogout"),
]
