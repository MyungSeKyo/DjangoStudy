from django.shortcuts import render
from django.views.generic import DetailView, ListView
from photo.models import Photo, Album

# Create your views here.


class AlbumLV(ListView):
    model = Album


class AlbumDV(DetailView):
    model = Album


class PhotoDV(DetailView):
    model = Photo
