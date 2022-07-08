from rest_framework import viewsets

from blog_app.models import News, Favorite, Comments
from .serializers import FavoriteSerializer, CommentsSerializer, NewsSerializer


class NewsModelViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentsModelViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class FavoritesModelViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer