from django.contrib.auth.models import AbstractUser
from django.db import models


class AbstractModel(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        abstract = True


class Genre(AbstractModel):
    pass


class Director(AbstractModel):
    pass


class Studio(AbstractModel):
    pass


class Ip(models.Model):
    ip = models.CharField(max_length=50)


class Anime(models.Model):
    STATUS_ANIME = (
        ('released', 'Вышел'),
        ('ongoing', 'Онгоинг'),
        ('announcement', 'Анонс'),
    )

    AGE_RATING = (
        ('six', '6+'),
        ('thirteen', '13+'),
        ('sixteen', '16+'),
        ('eighteen', '18+'),
    )

    SEASON_ANIME = (
        ('autumn', 'Осень'),
        ('winter', 'Зима'),
        ('spring', 'Весна'),
        ('summer', 'Лето'),
    )

    TYPE_ANIME = (
        ('series', 'Сериал'),
        ('feature_film', 'Полнометражный фильм'),
        ('short_film', 'Короткометражный фильм'),
        ('ova', 'OVA'),
        ('special', 'Special'),
        ('ona', 'ONA'),
    )

    title = models.CharField(max_length=250)
    second_title = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='posters/')
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    studios = models.ManyToManyField(Studio)
    year = models.CharField(max_length=4)
    total_series = models.PositiveIntegerField()
    status = models.CharField(max_length=12, choices=STATUS_ANIME)
    age_ratings = models.CharField(max_length=9, choices=AGE_RATING)
    season = models.CharField(max_length=7, choices=SEASON_ANIME)
    type = models.CharField(max_length=13, choices=TYPE_ANIME)
    views = models.ManyToManyField(Ip)
    slug = models.SlugField(unique=True)


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='comments')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)


class RatingStars(models.Model):
    value = models.PositiveIntegerField()


class Rating(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='ratings')
    star = models.ForeignKey(RatingStars, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='ratings')


class CustomUser(AbstractUser):
    avatar = models.ImageField(default='avatars/avatar.png', upload_to='avatars/')
    watching_now = models.ManyToManyField('WatchingNow')
    will_watch = models.ManyToManyField('WillWatch')
    viewed = models.ManyToManyField('Viewed')
    favorite = models.ManyToManyField('Favorite')


class AnimeList(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class WatchingNow(AnimeList):
    pass


class WillWatch(AnimeList):
    pass


class Viewed(AnimeList):
    pass


class Throw(AnimeList):
    pass


class Favorite(AnimeList):
    pass



