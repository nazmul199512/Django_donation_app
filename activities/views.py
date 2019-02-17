from django.shortcuts import render
from .models import WomenDevelopment, UrbanDevelopment, AwarenessSession, VocationalTraining, MedicalCamp


def women_development(request):
    query = WomenDevelopment.objects.all()
    context = {'query': query}
    return render(request, 'activities/women_development.html', context)


def urban_development(request):
    query = UrbanDevelopment.objects.all()
    context = {'query': query}
    return render(request, 'activities/urban_development.html', context)


def awareness_session(request):
    query = AwarenessSession.objects.all()
    context = {'query': query}
    return render(request, 'activities/awareness.html', context)


def vocational_training(request):
    query = VocationalTraining.objects.all()
    context = {'query': query}
    return render(request, 'activities/vocational.html', context)


def medical_camp(request):
    query = MedicalCamp.objects.all()
    context = {'query': query}
    return render(request, 'activities/medical.html', context)