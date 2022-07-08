from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormMixin
from django.urls import reverse, reverse_lazy

from .forms import LeftCommentsForm
from email_newsletter.forms import NewsletterForm
from email_newsletter.models import Newsletter
from .models import News, Favorite, Comments


class NewsListView(FormMixin, ListView):
    model = News
    context_object_name = "news_list"
    template_name = "base.html"

    form_class = NewsletterForm
    success_url = reverse_lazy('news-list-view')

    def post(self, request, *args, **kwargs):
        subscribers = Newsletter.objects.all()
        if subscribers.exists():
            return redirect('/')
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['newsletter_form'] = self.get_form()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NewsDetailView(FormMixin, DetailView):
    model = News
    template_name = "news_detail_view.html"
    slug_field = "slug"
    context_object_name = "news_detail"

    form_class = LeftCommentsForm

    def get_success_url(self):
        return reverse('news-detail', kwargs={'slug': self.object.slug})

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return reverse('news-detail', kwargs={'slug': self.object.slug})
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super(NewsDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = self.get_form()
        context['comments'] = Comments.objects.filter(blog=self.object)
        return context

    def get_initial(self):
        return {"user": self.request.user, "blog": self.object}

    def form_valid(self, form):
        form.save()
        return super(NewsDetailView, self).form_valid(form)


class AddFavoriteView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = "news-detail"

    def post(self, request, slug):
        blog = get_object_or_404(News, slug=slug)
        redirect_to_prev_page = redirect(reverse('news-detail', kwargs={'slug': slug}))
        favorite = Favorite.objects.filter(user=request.user, blog=blog)
        if not favorite.exists():
            favorite.create(user=request.user, blog=blog)
            return redirect_to_prev_page
        else:
            favorite.get(user=request.user, blog=blog).delete()
            return redirect_to_prev_page


class FavoriteListView(ListView):
    model = Favorite
    context_object_name = 'favorite_list'
    template_name = 'favorite_list.html'


class UserPostsView(ListView):
    model = News
    context_object_name = 'user_posts'
    template_name = 'user_post.html'

    def get_queryset(self):
        return News.objects.filter(author=self.request.user)