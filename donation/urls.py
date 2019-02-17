from django.conf.urls import url
from .views import volunteer_registration, payment_process, done, canceled, payment_process1


urlpatterns = [
      url('^volunteer/$', volunteer_registration, name='volunteer'),
      url('^donate/$', payment_process, name='donate'),
      url('^process/$', payment_process1, name='process'),
      url('^done/$', done, name='done'),
      url('^canceled/$', canceled, name='canceled'),

  ]