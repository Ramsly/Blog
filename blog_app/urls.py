from django.urls import path

from .views import \
    (NewsListView,
     NewsDetailView,
     FavoriteListView,
     AddFavoriteView,
     UserPostsView,
     )

urlpatterns = [
    path('user-posts/', UserPostsView.as_view(), name='user-post'),
    path('favorites/', FavoriteListView.as_view(), name='favorite-user-list'),
    path('<str:slug>/', NewsDetailView.as_view(), name='news-detail'),
    path('favorite/<str:slug>/', AddFavoriteView.as_view(), name='favorite'),
    path('', NewsListView.as_view(), name='news-list-view'),
]
