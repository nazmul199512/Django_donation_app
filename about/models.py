from django.db import models


class Profile(models.Model):
    organization_name = models.CharField(max_length=100)
    unit_of_Social_organ = models.CharField(max_length=100)
    established_year = models.IntegerField()
    organization_address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    registration_details = models.CharField(max_length=100)
    fcra_details = models.CharField(max_length=100)
    a_details = models.CharField(max_length=100)
    g_details = models.CharField(max_length=100)
    bank = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    account = models.CharField(max_length=100)
    isfs = models.CharField(max_length=1000)

    def __str__(self):
        return self.organization_name


class History(models.Model):
    title = models.CharField(max_length=10000)
    content = models.TextField()
    image = models.ImageField(blank=True, upload_to='about')

    def __str__(self):
        return self.title

