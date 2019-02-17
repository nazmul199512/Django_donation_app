from django.forms import ModelForm
from .models import VolunteerRegistration, Donation


class VolunteerRegistrationForm(ModelForm):
    class Meta:
        model = VolunteerRegistration
        fields = [
            'email',
            'first_name',
            'last_name',
            'address',
            'city',
            'state',
            'zip_pin_code',
            'country',
            'phone'
        ]


class DonationForm(ModelForm):
    class Meta:
        model = Donation
        fields = [
            'name',
            'email_id',
            'mobile_number',
            'choose_activity',
            'amount'
        ]