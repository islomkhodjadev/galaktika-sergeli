from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("courses", views.courses, name='courses'),
    path("teacher", views.teacher, name='teacher'),
    path("about", views.about, name='about'),
    path("blog", views.blog, name='blog'),
    path("contact", views.contact, name='contact')
]