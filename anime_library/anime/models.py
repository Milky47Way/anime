from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genres(models.Model):
    genre = models.CharField("Жанр", max_length=50)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"
        ordering = ['genre']

    def __str__(self):
        return self.genre

class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

    def __str__(self):
        return self.name

class DubStudio(models.Model):
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Студія дубляжу"
        verbose_name_plural = "Студії дубляжу"

    def __str__(self):
        return self.name

class Anime(models.Model):
    title = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='images/posters', verbose_name='Лого')
    description = models.TextField()

    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True, blank=True, related_name="anime")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True, related_name="authored_anime")
    dubStudio = models.ForeignKey(DubStudio, on_delete=models.SET_NULL, null=True)

    release = models.DateField(verbose_name="Дата релізу")
    trailer_url = models.URLField(blank=True)

    rating = models.DecimalField(max_digits=3, decimal_places=1, default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    class Meta:
        verbose_name = "Аніме"
        verbose_name_plural = "Аніме"

    def __str__(self):
        return self.title