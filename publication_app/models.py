from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)


class People(models.Model):
    name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    role = models.CharField(max_length=256, unique=True, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
