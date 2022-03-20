from django.db import models

# Create your models here.
from django.db import models
from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models.signals import post_save
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    hood_name = models.CharField(max_length=30)
    profile_pic = models.ImageField(upload_to='photos/', default='profile.jpg')
    phone_number = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.profile_pic.path)
        if img.height > 250 or img.width > 180:
            output_size = (220, 150)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

    def get_absolute_url(self):
        return reverse('aphood:update_profile', kwargs={'pk': self.pk})

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            profile = Profile.objects.create(user=kwargs['instance'])

    post_save.connect(create_profile, sender=User)

    def __str__(self):
        return f'{self.user.username} Profile'


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    picture = models.ImageField(upload_to='photos/', default='post.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('aphood:home')

class Neighborhood(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    rent_rates = models.IntegerField(default=0)
    description = models.CharField(max_length=30)
    closest_health_contact = models.IntegerField(default=0)
    closest_security_contact = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=30)
    business_pic = models.ImageField(upload_to='photos/', default='biz.jpg')
    description = models.TextField()
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('aphood:business')