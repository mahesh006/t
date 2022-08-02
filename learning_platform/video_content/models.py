from distutils.command.upload import upload
from django.db import models
from matplotlib.image import thumbnail
from matplotlib.pyplot import title

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    thumbnail = models.ImageField(upload_to=)
