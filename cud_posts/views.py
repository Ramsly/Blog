from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from blog_app.models import News
from .forms import CreatePostForm, UpdatePostForm


class CreatePostView(CreateView):
    model = News
    form_class = CreatePostForm
    template_name = 'cud_posts/create_post.html'

    def form_valid(self, form):
        form.save()
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('news-detail', kwargs={'slug': self.object.slug})

    def get_initial(self):
        return {'author': self.request.user}


class UpdatePostView(UpdateView):
    model = News
    slug_field = 'slug'
    form_class = UpdatePostForm
    context_object_name = 'post'
    template_name = 'cud_posts/update_post.html'

    def form_valid(self, form):
        form.save()
        return super(UpdatePostView, self).form_valid(form)

    def get_success_url(self):
        return reverse('news-detail', kwargs={'slug': self.object.slug})

    def get_initial(self):
        return {'author': self.request.user}


class DeletePostView(DeleteView):
    model = News
    slug_field = 'slug'
    context_object_name = 'post'
    template_name = 'cud_posts/delete_post.html'
    success_url = reverse_lazy("news-list-view")


