from django.shortcuts import render
from django.shortcuts import redirect
from .models import ContactForm, ContactAddress
from .forms import ContactFormAdmin


def contact_form(request):
    query = ContactAddress.objects.all()
    form = ContactFormAdmin(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        return redirect('/contact/contact/')
    context = {'form': form, 'query': query}
    return render(request, 'contact.html', context)
