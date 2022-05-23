from PIL import Image
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, unique=False, blank=False, null=False)
    text = models.TextField(blank=False, null=False)
    is_public = models.BooleanField(default=True)
    image = models.ImageField(null=True, blank=True)
    post_likes = models.IntegerField(default=0)


class People(models.Model):
    name = models.CharField(max_length=256, unique=False, blank=False, null=False)
    role = models.CharField(max_length=256, unique=True, blank=False, null=False)
    image = models.ImageField(null=True, blank=True)


class Comments(models.Model):
    comments_text = models.TextField()
    comments_post = models.ForeignKey(Post, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)