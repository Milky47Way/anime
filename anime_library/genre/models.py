from django.db import models

class Genres(models.Model):
    genre = models.CharField("Назва жанру", max_length=100, unique=True)

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанри"
        ordering = ['genre']

    def __str__(self):
        return self.genre