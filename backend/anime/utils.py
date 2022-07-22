from .models import WatchingNow, WillWatch, Throw, Favorite, Viewed, Anime


def add_anime_list(request):
    user = request.user
    anime_id = request.data['anime']
    anime = Anime.objects.get(id=anime_id)
    name_of_list = request.data['field']
    objects = {
        'WatchingNow': (WatchingNow, user.watching_now),
        'WillWatch': (WillWatch, user.will_watch),
        'Throw': (Throw, user.throw),
        'Favorite': (Favorite, user.favorite),
        'Viewed': (Viewed, user.viewed)
    }
    model = objects[name_of_list][0]
    field = objects[name_of_list][1]
    obj, created = model.objects.get_or_create(anime=anime)
    if obj in field.all():
        field.remove(obj)
    else:
        field.add(obj)
    if objects[name_of_list] == 'Favorite': 
        del objects[name_of_list]
    else:
        del objects[name_of_list]
    for v in objects.values():
        for object_ in v[1].all():
            if anime == object_.anime:
                v[1].remove(object_)
