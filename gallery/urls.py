from django.conf.urls import url
from .views import photo_upload, video_upload


urlpatterns = [
      url('^image/$', photo_upload, name='image'),
      url('^video/$', video_upload, name='video'),

      ]