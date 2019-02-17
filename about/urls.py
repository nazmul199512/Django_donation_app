from django.conf.urls import url
from .views import about_profile, about_history


urlpatterns = [
      url('^profile/', about_profile, name='profile'),
      url('^history/', about_history, name='history'),
]

