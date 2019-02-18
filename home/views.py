from django.shortcuts import render
from about.models import History
from activities.models import AwarenessSession, MedicalCamp, VocationalTraining
from donation.models import Donation
from .models import HomeImage


def home(request):
    query1 = History.objects.all().order_by('-id')
    query2 = AwarenessSession.objects.all().order_by('-id')
    query3 = MedicalCamp.objects.all().order_by('-id')
    query4 = VocationalTraining.objects.all().order_by('-id')
    query5 = Donation.objects.all().order_by('-id')
    context = {
        'query1': query1,
        'query2': query2,
        'query3': query3,
        'query4': query4,
        'query5': query5,
    }
    return render(request,"home.html", context)


def home_image(request):
    query = HomeImage.objects.all().order_by('-id')
    return render(request, 'home.html', {'query': query})