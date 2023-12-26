from django.contrib import admin
from .models import Quotes, Learners_count, Course, Testimonials, Blog, Event, Teacher, About, Students

class QuotesAdmin(admin.ModelAdmin):
    
    
    
        
    
    list_display = ('quote', 'image')
    search_fields = ('quote',)
    exclude = ('img_webp',)

class LearnersCountAdmin(admin.ModelAdmin):
    
    
    
        
    list_display = ('type', 'count')
    search_fields = ('type',)
    exclude = ('img_webp',)

class CourseAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('name', 'about', 'image')
    search_fields = ('name',)
    exclude = ('img_webp',)

class TestimonialsAdmin(admin.ModelAdmin):
    
   
    
    list_display = ('name', 'type', 'feedback', 'image')
    search_fields = ('name', 'type')
    exclude = ('img_webp',)

class BlogAdmin(admin.ModelAdmin):
    
    
    
    
    list_display = ('title', 'date', 'content', 'image')
    search_fields = ('title', 'content')
    exclude = ('img_webp',)

class EventAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('title', 'date', 'content', 'feedback', 'image')
    search_fields = ('title', 'content')
    exclude = ('img_webp',)

class TeacherAdmin(admin.ModelAdmin):
    
    
    
    list_display = ('name', 'about', 'image')
    search_fields = ('name',)
    exclude = ('img_webp',)

class AboutAdmin(admin.ModelAdmin):
    
    
    
    
    list_display = ('welcome', 'content', 'image')
    search_fields = ('welcome',)
    exclude = ('img_webp',)

class StudentsAdmin(admin.ModelAdmin):
    
    
    
    
    
    list_display = ('name', 'surname', 'phone', 'active')
    search_fields = ('name', 'surname')
    exclude = ('img_webp',)

# Registering models with the admin site
admin.site.register(Quotes, QuotesAdmin)
admin.site.register(Learners_count, LearnersCountAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Testimonials, TestimonialsAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Students, StudentsAdmin)
