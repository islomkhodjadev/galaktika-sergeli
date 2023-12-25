from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Quotes(models.Model):
    image = models.ImageField(upload_to="index/quotes/img")
    img_webp = models.ImageField(blank=True, upload_to="index/quotes/img_webp")
    quote = models.CharField(max_length=200)

    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)


class Learners_count(models.Model):
    type = models.CharField(max_length=50)
    count = models.IntegerField()
    
class Course(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=400)
    image = models.ImageField(upload_to="index/courses/img")
    img_webp = models.ImageField(blank=True, upload_to="index/courses/img_webp")
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)


class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    feedback = models.TextField(max_length=200)
    image = models.ImageField(upload_to="index/testimonials/img")
    img_webp = models.ImageField(blank=True, upload_to="index/testimonials/img_webp")
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(max_length=500)

class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    content = models.TextField(max_length=500)
    feedback = models.IntegerField()
    image = models.ImageField(upload_to='index/events/img')
    img_webp = models.ImageField(blank=True, upload_to="index/events/img_webp")
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(max_length=400)
    image = models.ImageField(upload_to="index/teachers/img")
    img_webp = models.ImageField(blank=True, upload_to="index/teachers/img_webp")
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)


class About(models.Model):
    __limit = True
    
    welcome = models.CharField(max_length = 50)
    content = models.TextField(max_length = 500)
    image = models.ImageField(upload_to="index/about/img")
    img_webp = models.ImageField(blank=True, upload_to="index/about/img_webp")
    
    def __new__(cls, *args, **kwargs):
        if cls.__limit:
            cls.__limit = False
            super().__new__(cls)
    
    def save(self, *args, **kwargs):
        # Convert image to WebP and save
        if self.image:
            # Open the image using Pillow
            pil_image = Image.open(self.image)
            # Convert the image to RGB mode if it's not
            if pil_image.mode != 'RGB':
                pil_image = pil_image.convert('RGB')
            # Save the image in a BytesIO object
            image_io = BytesIO()
            pil_image.save(image_io, format='WEBP')
            # Create a Django-friendly ContentFile
            webp_image = ContentFile(image_io.getvalue())
            # Save to img_webp field
            self.img_webp.save(f'{self.image.name.split(".")[0]}.webp', webp_image, save=False)

        super().save(*args, **kwargs)




class Students(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=13)
    courses = models.ManyToManyField(Course)
    teachers = models.ManyToManyField(Teacher)
    active = models.BooleanField(blank=True, default=False)
