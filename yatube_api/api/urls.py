from django.urls import path, include
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'posts/(?P<post_id>[\w.@+-]+)/comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
