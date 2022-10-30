"""Set your api URLs here."""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentPostViewSet, FollowViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()
router_v1.register('follow', FollowViewSet, basename='follow')
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register(r'posts/(?P<post_id>\d+)/comments', CommentPostViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
