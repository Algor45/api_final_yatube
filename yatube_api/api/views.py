"""Write your api app view functions here."""

from django.shortcuts import get_object_or_404
from posts.models import Group, Post, User
from rest_framework import filters, mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated

from .permissions import AuthorPermissionOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)


class GroupRetrieveListViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               viewsets.GenericViewSet):
    """Mixin RetriveList."""

    pass


class PostViewSet(viewsets.ModelViewSet):
    """Viewset для модели Post и PostSerializer."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [AuthorPermissionOrReadOnly, ]
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Переопределение метода create для PostViewSet."""
        serializer.save(author=self.request.user)


class GroupViewSet(GroupRetrieveListViewSet):
    """Viewset для модели Group и GroupSerializer."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AuthorPermissionOrReadOnly]


class CommentPostViewSet(viewsets.ModelViewSet):
    """Viewset для модели Comment и CommentSerializer."""

    serializer_class = CommentSerializer

    permission_classes = [AuthorPermissionOrReadOnly, ]

    def perform_create(self, serializer):
        """Переопределение метода create для CommentPostViewSet."""
        serializer.save(author=self.request.user)

    def get_queryset(self):
        """Переопределение метода get_queryset для CommenPostViewSet."""
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(viewsets.ModelViewSet):
    """Viewset для модели Follow и FollowSerializer."""

    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticated, ]
    filter_backends = [filters.SearchFilter, ]
    search_fields = ('user__username', 'following__username')

    def perform_create(self, serializer):
        """Переопределение метода create для FollowViewSet."""
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """Переопределение метода get_queryset для FollowViewSet."""
        user = get_object_or_404(User, username=self.request.user.username)
        return user.follower
