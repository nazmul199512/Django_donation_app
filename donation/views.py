from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .forms import VolunteerRegistrationForm, DonationForm
from .models import VolunteerRegistration, Volunteer, Donation
from paypal.standard.forms import PayPalPaymentsForm
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings
from django.contrib import messages
from .decorators import check_recaptcha


def volunteer_registration(request):
    query = Volunteer.objects.all()
    form = VolunteerRegistrationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/donation/volunteer/')
    context = {"form": form, 'query': query}
    return render(request, "volunteer_form.html", context)


@check_recaptcha
def payment_process(request):
    form = DonationForm(request.POST or None)
    if form.is_valid() and request.recaptcha_is_valid:
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        messages.success(request, 'Successfully passed captcha !')
        return redirect('/donation/donate/')
    context = {'form': form}
    return render(request, 'donation.html', context)


def payment_process1(request):
    query_set = Donation.objects.all().order_by('-id')
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': query_set.amount,
        'invoice': str(query_set.name),
        'currency_code': 'USD',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('/donation/done/')),
        'cancel_return': 'http://{}{}'.format(host, reverse('/donation/canceled/')),

     }
    form = PayPalPaymentsForm(initial=paypal_dict)

    return render(request, 'process.html', {'form': form, })


@csrf_exempt
def done(request):
    return render(request, 'done.html', {})


@csrf_exempt
def canceled(request):
    return render(request, 'canceled.html', {})



