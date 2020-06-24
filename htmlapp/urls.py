from . import views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('home', views.Homepageview.as_view(), name='home'), # pylint: disable=maybe-no-member
    path('about', views.AboutPage.as_view(), name='about'),
    path('contact', views.ContactPage.as_view(), name='contact'),
    
]