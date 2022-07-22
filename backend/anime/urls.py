from django.urls import path

from .views import AnimeActualListApiView, AnimeDetailApiView, UserAnimeListUpdateApiView, RatingCreateUpdateApiView

urlpatterns = [
    path('anime/list/', AnimeActualListApiView.as_view(), name='anime-list'),
    path('anime/rating/', RatingCreateUpdateApiView.as_view()),
    path('anime/<slug:slug>/', AnimeDetailApiView.as_view(), name='anime-detail'),
    path('user/update/anime-list/', UserAnimeListUpdateApiView.as_view()),
    path('user/get/<str:username>/', UserAnimeListUpdateApiView.as_view()),
]