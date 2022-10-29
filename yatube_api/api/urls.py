"""Set your api URLs here."""

from django.db import router
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentPostViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentPostViewSet,
                basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
