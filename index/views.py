from django.shortcuts import render, redirect
from . import models, forms
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
    abouts = models.About.objects.first()
    events = models.Event.objects.all()[:3]
    counts = models.Learners_count.objects.all()
    print(abouts)
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

def contact(request, course_id=None):
    
    
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        if course_id:
            form = forms.ContactForm()
            form.fields['courses'].initial = [models.Course.objects.get(pk=course_id)]
            
        else:
            form = forms.ContactForm()
            
        
        
    context = {
        'active':"contact",
        "quotes": quotes,
        'form':form
    }
    
    return render(request, "index/contact.html", context=context)



def post(request, id, type):
    context = {
        'active':"blog",
        "quotes": quotes,
    }
    
    if type == "blog":
        post = models.Blog.objects.get(pk=id)
    elif type == "event":
        post = models.Event.objects.get(pk=id) 
    
    else:
        post = None
    
    context["post"] = post
    
    return render(request, "index/post.html", context=context)