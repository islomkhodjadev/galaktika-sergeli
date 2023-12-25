from django.shortcuts import render
from . import models

# Create your views here.
quotes = models.Quotes.objects.all()

def index(request):
    
    counts = models.Learners_count.objects.all()
    courses = models.Course.objects.all()[:3]
    testimonals = models.Testimonials.objects.all()
    blogs = models.Blog.objects.all()[:3]
    events = models.Event.objects.all()[:3]
    
    
    context = {
        'active':"index",
        "quotes": quotes,
        "counts": counts,
        "courses":courses,
        "testimonials": testimonals,
        "blogs":blogs,
        "events": events,
    }
    
    return render(request, "index/home.html", context=context)

def courses(request):
    courses = models.Course.objects.all()
    
    
    
    
    context = {
        'active':"courses",
        "courses":courses,
        "quotes": quotes,
    }
    
    
    
    return render(request, "index/courses.html", context=context)

def teacher(request):
    teachers = models.Teacher.objects.all()
    
    context = {
        'active':"teacher",
        "teachers":teachers,
        "quotes": quotes,
    }
    
    return render(request, "index/teachers.html", context=context)

def about(request):
    abouts = models.About.objects.all()[:1]
    events = models.Event.objects.all()[:3]
    counts = models.Learners_count.objects.all()
    
    context = {
        'active':"about",
        "about":abouts,
        "events": events,
        "counts": counts,
        "quotes": quotes,
    }
    
    return render(request, "index/about.html", context=context)

def blog(request):
    blogs = models.Blog.objects.all()
    events = models.Event.objects.all()
    
    context = {
        'active':"blog",
        "blogs":blogs,
        "events": events,
        "quotes": quotes,
    }
    
    return render(request, "index/blog.html", context=context)

def contact(request):
    
    context = {
        'active':"contact",
        "quotes": quotes,
    }
    
    return render(request, "index/contact.html", context=context)
