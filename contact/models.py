from django.db import models


class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return self.name


class ContactAddress(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    phone = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.title