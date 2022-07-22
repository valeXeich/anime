from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers

from .models import Anime, Comment, CustomUser, WatchingNow, Rating


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ["password", "username", "email"]
    
    def create(self, validated_data):
        return CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            slug=validated_data['username']
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)
    created_date = serializers.SlugRelatedField(slug_field='year', read_only=True)

    class Meta:
        model = Comment
        fields = ['author', 'content', 'created_date', 'id']


class AnimeSerializer(serializers.ModelSerializer):
    comments = serializers.IntegerField(source='get_total_comments')
    views = serializers.IntegerField(source='get_total_views')
    type = serializers.CharField(source='get_type_display')
    release_date = serializers.SlugRelatedField(slug_field='year', read_only=True)

    class Meta:
        model = Anime
        fields = [
            'total_series',
            'title',
            'release_date',
            'type',
            'poster',
            'comments',
            'slug',
            'views'
        ]
    
    def get_total_comments(self, obj):
        return obj.comments.count()
    

class AnimeDetailSerializer(serializers.ModelSerializer):
    views = serializers.IntegerField(source='get_total_views')
    studios = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    genres = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    directors = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)
    comments = CommentSerializer(many=True)
    status = serializers.CharField(source='get_status_display')
    age_ratings = serializers.CharField(source='get_age_ratings_display')
    total_comments = serializers.IntegerField(source='get_total_comments')
    type = serializers.CharField(source='get_type_display')
    similar_anime = AnimeSerializer(source='get_similar_anime', many=True)
    avg_rating = serializers.FloatField(source='get_avg_rating')
    
    class Meta:
        model = Anime
        fields = [
            'id',
            'title',
            'second_title',
            'type',
            'studios',
            'release_date',
            'genres',
            'directors',
            'status',
            'age_ratings',
            'views',
            'comments',
            'total_comments',
            'description',
            'similar_anime',
            'avg_rating'
        ]
    
class AnimeListSerizalizer(serializers.ModelSerializer):
    anime = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = WatchingNow
        fields = ['anime']


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    anime = serializers.SlugRelatedField(slug_field='title', read_only=True)
    star = serializers.SlugRelatedField(slug_field='value', read_only=True)

    class Meta:
        model = Rating
        fields = ['anime', 'star', 'user']
        read_only_fields = ['user']
    
    
class UserSerializer(serializers.ModelSerializer):
    watching_now = serializers.SerializerMethodField()
    will_watch = serializers.SerializerMethodField()
    viewed = serializers.SerializerMethodField()
    throw = serializers.SerializerMethodField()
    favorite = serializers.SerializerMethodField()
    
    class Meta:
        model = CustomUser
        fields = [
            'username',
            'avatar',
            'watching_now', 
            'will_watch',
            'throw',
            'favorite',
            'viewed'
        ]
    
    
    def get_watching_now(self, obj):
        return [object_.anime.title for object_ in obj.watching_now.all()]
    
    def get_will_watch(self, obj):
        return [object_.anime.title for object_ in obj.will_watch.all()]
    
    def get_viewed(self, obj):
        return [object_.anime.title for object_ in obj.viewed.all()]
    
    def get_throw(self, obj):
        return [object_.anime.title for object_ in obj.throw.all()]
    
    def get_favorite(self, obj):
        return [object_.anime.title for object_ in obj.favorite.all()]
    
   