from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Quotes(models.Model):
    image = models.ImageField(upload_to="index/quotes/img", verbose_name="Rasm")
    img_webp = models.ImageField(blank=True, upload_to="index/quotes/img_webp")
    quote = models.CharField(max_length=200, verbose_name="Maqol")

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

    def __str__(self):
        return self.quote
    
    class Meta:
        verbose_name = "Maqollar"
        verbose_name_plural = "Maqollar"
        
    
class Learners_count(models.Model):
    
    
    class Meta:
        verbose_name = "Statistika"
        verbose_name_plural = "Statistika"
        
    
    type = models.CharField(max_length=50, verbose_name="Turkumi")
    count = models.IntegerField(verbose_name="Soni")
    def __str__(self):
        return self.type
    
    
class Course(models.Model):
    
    class Meta:
        verbose_name = "Kurslar"
        verbose_name_plural = "Kurslar"
    
    
    name = models.CharField(max_length=100, verbose_name="Kurs ismi")
    about = models.TextField(max_length=400, verbose_name='Haqida')
    image = models.ImageField(upload_to="index/courses/img", verbose_name="rasm")
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
    def __str__(self):
        return self.name

class Testimonials(models.Model):
    
    class Meta:
       verbose_name = "Natijalar"
       verbose_name_plural = "Natijalar"
    
    
    
    name = models.CharField(max_length=50, verbose_name="ism")
    type = models.CharField(max_length=50, verbose_name="turi")
    feedback = models.TextField(max_length=200, verbose_name="Fikri")
    image = models.ImageField(upload_to="index/testimonials/img", verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/testimonials/img_webp")
    def __str__(self):
        return self.name
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
    
    
    
    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"
    
    title = models.CharField(max_length=100, verbose_name='sarlavha')
    date = models.DateField(auto_now=True, verbose_name='kuni')
    content = models.TextField(max_length=500, verbose_name='maqola')
    image = models.ImageField(upload_to='index/events/img', verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/events/img_webp")
    def __str__(self):
        return self.title
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
        
        
class Event(models.Model):
    
    class Meta:
        verbose_name = "Tadbir"
        verbose_name_plural = "Tadbirlar"
    
    
    
    
    title = models.CharField(max_length=100, verbose_name='sarlavha')
    date = models.DateField(auto_now=True, verbose_name='kuni')
    content = models.TextField(max_length=500, verbose_name='tadbir haqida')
    feedback = models.IntegerField(verbose_name="Qatnashganlar soni")
    image = models.ImageField(upload_to='index/events/img', verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/events/img_webp")
    def __str__(self):
        return self.title
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
    
    
    class Meta:
        verbose_name = "O'qituvchilar"
        verbose_name_plural = "O'qituvchilar"
    
    
    
    
    telegram = models.CharField(max_length=100, blank=True)
    instagram = models.CharField(max_length=100, blank=True)
    facebook = models.CharField(max_length=100, blank=True)
    twitter = models.CharField(max_length=100, blank=True)
    github = models.CharField(max_length=100, blank=True)
    
    name = models.CharField(max_length=100, verbose_name='ism')
    about = models.TextField(max_length=400, verbose_name='haqida')
    image = models.ImageField(upload_to="index/teachers/img", verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/teachers/img_webp")
    def __str__(self):
        return self.name
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
    def __str__(self):
        return self.welcome
    
    welcome = models.CharField(max_length = 50, verbose_name='xush kelibsiz')
    content = models.TextField(max_length = 500, verbose_name='haqida')
    image = models.ImageField(upload_to="index/about/img", verbose_name='rasm')
    img_webp = models.ImageField(blank=True, upload_to="index/about/img_webp")
    
    class Meta:
        verbose_name = "Haqida"
        verbose_name_plural = "Haqida"

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
    
    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Studentlar"
    
    
    def __str__(self):
        return self.name
    name = models.CharField(max_length=50, verbose_name='student ismi')
    surname = models.CharField(max_length=50, verbose_name='student familiyasi')
    phone = models.CharField(max_length=13, verbose_name='nomer')
    courses = models.ManyToManyField(Course, blank=True, verbose_name="yozilgan kurslari")
    teachers = models.ManyToManyField(Teacher, blank=True, verbose_name="o'qituvchilari")
    active = models.BooleanField(blank=True, default=False, verbose_name="O'qimoqda")
