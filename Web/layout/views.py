from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

def homepage(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def redirect_homepage(request):
    return redirect('homepage')

# Create your views here.
