from audioop import add
from django.db.models import Count
from django.http import JsonResponse
from rest_framework import generics, filters, views, permissions
from rest_framework.response import Response

from .models import Anime, CustomUser, Rating, RatingStars
from .serializers import AnimeSerializer, AnimeDetailSerializer, UserSerializer, RatingSerializer
from .utils import add_anime_list


class AnimeActualListApiView(generics.ListAPIView):
    queryset = Anime.objects.annotate(
        views_cnt=Count('views'), comm_cnt=Count('comments')
    )
    serializer_class = AnimeSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['views_cnt', 'comm_cnt', 'release_date', 'created_date']


class AnimeDetailApiView(generics.RetrieveAPIView):
    queryset = Anime.objects.all()
    serializer_class = AnimeDetailSerializer
    lookup_field = 'slug'


class RatingCreateUpdateApiView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    
    def create(self, request, *args, **kwargs):
        star = RatingStars.objects.get(value=request.data['star'])
        anime = Anime.objects.get(id=request.data['anime'])
        rating, created = Rating.objects.update_or_create(
            anime=anime,
            user=request.user,
            defaults={'star': star}
        )
        serializer = self.serializer_class(rating)
        return Response(serializer.data)


class UserAnimeListUpdateApiView(views.APIView):

    @staticmethod
    def validate(data):
        try:
            Anime.objects.get(id=data['anime'])
        except:
            return False
        if data['field'] in ['WatchingNow', 'WillWatch', 'Viewed', 'Favorite', 'Throw'] and isinstance(data['anime'], int):
            return True
        else:
            return False

    def patch(self, request):
        if self.validate:
            add_anime_list(request=request)
            return JsonResponse(data={'response': 'List of anime was updated'})
        else:
            return JsonResponse(data={'response': 'Something went wrond'})
    
    def get(self, request, username):
        user = CustomUser.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)