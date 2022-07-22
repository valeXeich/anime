from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from .models import Anime, Genre, Studio, Director

class AnimeTest(APITestCase):

    def setUp(self):
        anime_title = ['bleach', 'naruto']
        genre = Genre.objects.create(name='magic')
        studio = Studio.objects.create(name='MAPPA')
        director = Director.objects.create(name='Kubo')
        for title in anime_title:
            anime = Anime.objects.create(
            title=title,
            second_title='bleach 2',
            poster='bleach.img',
            release_date='2004-04-05',
            total_series=366,
            status='released',
            age_ratings='sixteen',
            season='autumn',
            type='series',
            description='The best hero',
            slug=title
        )
            anime.genres.add(genre)
            anime.studios.add(studio)
            anime.directors.add(director)

    def test_anime_list(self):
        response = self.client.get(reverse('anime-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertTrue({
            'title': 'bleach',
            'poster': 'http://testserver/media/bleach.img',
            'release_date': 2004,
            'total_series': 366,
            'type': 'Сериал',
            'comments': 0,
            'slug': 'bleach',
            'views': 0
        } in response.json())

    def test_anime_detail(self):
        response = self.client.get(reverse('anime-detail', kwargs={'slug': 'bleach'}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['title'], 'bleach')
        self.assertEqual(response.json()['genres'], ['magic'])





