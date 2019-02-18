from django.db import models


class HomeImage(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, upload_to='home')

    def __str__(self):
        return self.title
