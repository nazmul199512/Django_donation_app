from django.conf.urls import url
from .views import contact_form


urlpatterns = [
      url('^contact/$', contact_form, name='contact'),


      ]