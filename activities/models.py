from django.db import models


class WomenDevelopment(models.Model):
    title = models.CharField(max_length=100)
    objectives = models.CharField(max_length=1000)
    target_people = models.CharField(max_length=150)
    target_areas = models.CharField(max_length=150)
    problems = models.CharField(max_length=200)
    activities = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title


class UrbanDevelopment(models.Model):
    title = models.CharField(max_length=100)
    objectives = models.CharField(max_length=1000, blank=True)
    target_areas = models.CharField(max_length=150)
    problems = models.TextField()
    activities = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title


class AwarenessSession(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title


class MedicalCamp(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title


class VocationalTraining(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to='gallery', blank=True)

    def __str__(self):
        return self.title