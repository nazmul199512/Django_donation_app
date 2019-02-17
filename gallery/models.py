from django.db import models
from django.utils import timezone


class Gallery(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='gallery')
    upload_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=150)
    embed_code = models.TextField()
    add_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title




