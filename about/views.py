from django.shortcuts import render
from .models import Profile, History


def about_profile(request):
    template_name = 'about/profile.html'
    query = Profile.objects.all()
    context = {
        'query': query
    }
    return render(request, template_name, context)


def about_history(request):
    template_name = 'about/history.html'
    query = History.objects.all()
    context = {
        'query': query
    }
    return render(request, template_name, context)