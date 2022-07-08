from django.urls import path

from custom_user_app.views import SignUpView, UserDetailView, UserListView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('', UserListView.as_view(), name='user-list'),
    path('<str:slug>/', UserDetailView.as_view(), name='user-detail'),
]
