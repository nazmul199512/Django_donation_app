from django.contrib import admin
from .models import ContactForm, ContactAddress


admin.site.register(ContactAddress),
admin.site.register(ContactForm),
