from django.shortcuts import render
from django.http import HttpResponse
from . import templates
from django.views.generic import TemplateView

class Homepageview(TemplateView):
    template_name = 'indexi.html'



""" Menyra e dyte
def index(request):
    return render(request, 'indexi.html')
"""

class AboutPage(TemplateView):
    template_name = 'about.html'

class ContactPage(TemplateView):
    template_name = 'contact.html'