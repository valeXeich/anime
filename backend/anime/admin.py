from django.contrib import admin

from .models import (
    Anime,
    Genre,
    Director,
    Studio,
    Comment,
    Rating,
    RatingStars,
    Ip,
    CustomUser,
    WatchingNow,
    WillWatch,
    Viewed,
    Throw,
    Favorite
)


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Studio)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(RatingStars)
admin.site.register(Ip)
admin.site.register(CustomUser)
admin.site.register(WatchingNow)
admin.site.register(WillWatch)
admin.site.register(Viewed)
admin.site.register(Throw)
admin.site.register(Favorite)
