from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentsModelViewSet, FavoritesModelViewSet, NewsModelViewSet

router = DefaultRouter()
router.register(r'comments', CommentsModelViewSet)
router.register(r'favorites', FavoritesModelViewSet)
router.register(r'news', NewsModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
