from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import DateTimeField


class User(AbstractUser):
    pass

class Resource(models.Model):
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=2500)
    url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey("Category", blank=True, null=True)

    def __str__(self):
        return f"{self.title}, {self.authors}, {self.description}"

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=True, unique=True)

class Favorite(model.Models):
    created_at = models.DateTimeField(null=True, blank=True)