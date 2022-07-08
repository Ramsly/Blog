from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from custom_user_app.forms import CustomUserCreationForm
from custom_user_app.models import CustomUser


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('news-list-view')
    template_name = "registration/signup.html"

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class UserDetailView(DetailView):
    model = CustomUser
    context_object_name = 'users_detail'
    template_name = 'user_detail.html'
    slug_field = 'slug'


class UserListView(ListView):
    model = CustomUser
    context_object_name = 'users_list'
    template_name = 'user_list.html'
