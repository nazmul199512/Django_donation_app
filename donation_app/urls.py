"""donation_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('home.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^activities/', include('activities.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^donation/', include('donation.urls')),

    url(r'^login/$', LoginView.as_view(template_name='login.html'), name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


