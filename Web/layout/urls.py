from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.redirect_homepage),
    path('homepage', views.homepage, name='homepage'),
    path('about', views.about, name='about'),
]