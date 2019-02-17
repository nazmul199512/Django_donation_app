from django.conf.urls import url
from .views import women_development, urban_development, awareness_session, medical_camp, vocational_training


urlpatterns = [
      url('^women-dev/$', women_development, name='women-dev'),
      url('^urban-dev/$', urban_development, name='urban-dev'),
      url('^awareness/$', awareness_session, name='awareness'),
      url('^medical-camp/$', medical_camp, name='medical'),
      url('^vocational-training/$', vocational_training, name='vocational'),

      ]


