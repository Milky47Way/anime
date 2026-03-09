from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Anime

template_name = "anime/index.html"
context_object_name = "anime"
queryset = Anime.objects.order_by('-release')

class AnimeListView(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Anime.objects.filter(title__icontains=query)
        return Anime.objects.all().order_by('-release')


class GenreAnimeListView(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Anime.objects.filter(genre_id=self.kwargs['genre_id'])

class YearAnimeListView(ListView):
    model = Anime
    template_name = 'anime/index.html'
    context_object_name = 'anime'

    def get_queryset(self):
        year = self.kwargs.get('year')
        return Anime.objects.filter(release__year=year).order_by('-release')


    def get_context_data(self, **kwargs):
        year = self.kwargs.get('year')
        return Anime.objects.filter(release__year=year).order_by('-release')