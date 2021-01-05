from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects', views.projects, name='projects'),
    path('certifications', views.certifications, name='certifications'),
    path('about', views.about, name='about'),
    path('skills', views.skills, name='skills'),
]