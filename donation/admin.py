from django.contrib import admin
from .models import VolunteerRegistration, Volunteer, Donation


admin.site.register(VolunteerRegistration),
admin.site.register(Volunteer),
admin.site.register(Donation),
