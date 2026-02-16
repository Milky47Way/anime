from django.db import models
from django.contrib.auth.models import User


class Genres(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Anime(models.Model):
    title = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='images/posters', verbose_name='Лого')
    description = models.CharField(max_length=50)
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True, blank=True, related_name="anime")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="anime")
    release = models.DateTimeField


    def __str__(self):
        return self.title

class DubStudio(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Image(models.Model):


class Trailer(models.Model):


class Rating(models.Model):