from django.shortcuts import render
from django.http import HttpResponse
from .models import cartoon, movie, music


def index(request):
    return render(request, 'calen/index.html')

def cartoons(request):
    cartoons = cartoon.objects.all()
    return render(request, 'calen/cartoon_details.html', {'cartoons':cartoons})

def movies(request):
    movies = movie.objects.all()
    return render(request, 'calen/movie_details.html', {'movies':movies})

def music(request):
    return render(request, 'calen/music_details.html')
