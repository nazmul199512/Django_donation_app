from django.shortcuts import render
from .models import Gallery, Video


def photo_upload(request):
    query = Gallery.objects.all().order_by('-upload_date')
    context = {'query': query}
    return render(request, 'gallery/image.html', context)


def video_upload(request):
    query = Video.objects.all().order_by('-id')
    context = {'query': query}
    return render(request, 'gallery/video.html', context)




