from django.forms import ModelForm
from .models import ContactForm


class ContactFormAdmin(ModelForm):
    class Meta:
        model = ContactForm
        fields = [
            'name',
            'mobile',
            'email',
            'text',
        ]
