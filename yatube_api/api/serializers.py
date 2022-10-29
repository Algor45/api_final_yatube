from posts.models import Comment, Follow, Group, Post, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


class PostSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Post."""

    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        """Meta настройки сериалайзера для модели Post."""

        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Group."""

    class Meta:
        """Meta настройки сериалайзера для модели Group."""

        fields = ('id', 'title', 'slug', 'description')
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Comment."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        """Meta настройки сериалайзера для модели Comment."""

        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    """Сериалайзер для модели Follow."""

    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault()
    )

    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
    )

    class Meta:
        """Meta настройки сериалайзера для модели Follow."""

        fields = ('user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
                message='Подписка уже активна.')
        ]

    def validate(self, data):
        """Функция валидации выявляет попытку подписаться на себя самого."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Невозможно подписаться на себя самого!')
        return data
