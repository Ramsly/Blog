from django.urls import path

from .views import CreatePostView, UpdatePostView, DeletePostView


urlpatterns = [
    path('create-post/', CreatePostView.as_view(), name='create-post'),
    path('delete-post/<str:slug>', DeletePostView.as_view(), name='delete-post'),
    path('update-post/<str:slug>', UpdatePostView.as_view(), name='update-post'),
]
