from django.urls import reverse
from tabnanny import verbose
from django.db import models
from .validators import file_size
from django.contrib.auth.models import AbstractUser

# Create your models here.
# Sport
class Poets(models.Model):
    name = models.CharField( max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    

class Labours(models.Model):
    name = models.CharField(max_length=50)
    labour = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Heroes(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")

class Writers(models.Model):
    fullname = models.CharField(max_length=50)
    photo = models.CharField(max_length=10000)
    text = models.CharField(max_length=10000)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    




class News(models.Model):
    title = models.CharField('Title', max_length=250)
    anons = models.CharField('Text', max_length=250)
    full_text = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    # def get_absolute_url(self):
    #     return f'/news/{self.id}'
    def get_absolute_url(self):
        return reverse('news-update', kwargs={'post_slug': self.slug})

class Meta:
    verbose_name = 'Новость'
    verbose_name_plural = 'Новости'


class Post(models.Model):
    
    text = models.TextField(max_length=5000)
    name=models.CharField(max_length=50)
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y", validators=[file_size])
    
    def __str__(self):
        return self.caption


