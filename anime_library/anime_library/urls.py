"""
URL configuration for anime_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import  path, include, AnimeDetailView, GenreAnimeListView, admin
# from .views import *


app_name = "anime"

urlpatterns = {
    path("admin/", admin.site.urls),
    path("", include('anime.urls')),
    path("review/", include("review.urls")),
    path("characters/", include("characters.urls")),
    path("user/", include("user.urls")),

    path('anime/<int:pk>/', AnimeDetailView.as_view(), name='anime_detail'),
    path('genre/<int:genre_id>/', GenreAnimeListView.as_view(), name='genre_filter'),

}