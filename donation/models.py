from django.db import models


class VolunteerRegistration(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_pin_code = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Volunteer(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


class Donation(models.Model):
    CHOOSE_ACTIVITY = (
        ('W', 'WOMEN DEVELOPMENT'),
        ('A', 'AWARENESS SESSION'),
        ('M', 'MEDICAL CAMP'),
        ('V', 'VOCATION TRAINING'),
    )
    name = models.CharField(max_length=150)
    email_id = models.EmailField()
    mobile_number = models.CharField(max_length=150)
    choose_activity = models.CharField(max_length=4, choices=CHOOSE_ACTIVITY)
    amount = models.IntegerField()

    def __str__(self):
        return self.name
