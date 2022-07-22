from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Avg


class AbstractModel(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        abstract = True


class Genre(AbstractModel):
    pass

    def __str__(self) -> str:
        return self.name


class Director(AbstractModel):
    pass

    def __str__(self) -> str:
        return self.name


class Studio(AbstractModel):
    pass

    def __str__(self) -> str:
        return self.name


class Ip(models.Model):
    ip = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.ip


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
    release_date = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    total_series = models.PositiveIntegerField()
    status = models.CharField(max_length=12, choices=STATUS_ANIME)
    age_ratings = models.CharField(max_length=9, choices=AGE_RATING)
    season = models.CharField(max_length=7, choices=SEASON_ANIME)
    type = models.CharField(max_length=13, choices=TYPE_ANIME)
    views = models.ManyToManyField(Ip, blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def get_total_views(self):
        return self.views.count()
    
    def get_total_comments(self):
        return self.comments.count()
    
    def get_similar_anime(self):
        genres = self.genres.all()
        similar_anime = Anime.objects.filter(genres__in=genres).exclude(
            id=self.id).distinct()[:4]
        return similar_anime
    
    def get_avg_rating(self):
        return self.ratings.aggregate(Avg('star')).get('star__avg')

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='comments')
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.author.username


class RatingStars(models.Model):
    value = models.PositiveIntegerField()

    class Meta:
        ordering = ['-value']

    def __str__(self):
        return f'{self.value}'


class Rating(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='ratings')
    star = models.ForeignKey(RatingStars, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='ratings')

    def __str__(self):
        return f'{self.user}, Звезда: {self.star}, Аниме: {self.anime}'


class CustomUser(AbstractUser):
    avatar = models.ImageField(default='avatars/avatar.png', upload_to='avatars/')
    watching_now = models.ManyToManyField('WatchingNow', blank=True)
    will_watch = models.ManyToManyField('WillWatch', blank=True)
    viewed = models.ManyToManyField('Viewed', blank=True)
    favorite = models.ManyToManyField('Favorite', blank=True)
    throw = models.ManyToManyField('Throw', blank=True)


class AnimeList(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.anime.title


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



