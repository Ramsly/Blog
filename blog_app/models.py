from django.db import models
from django.urls import reverse

from custom_user_app.models import CustomUser


class News(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    text = models.TextField(max_length=5000, default="")
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, db_index=True)
    slug = models.SlugField(unique=True, default="")

    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title

    def get_news_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.slug})

    def get_author_absolute_url(self):
        return reverse('user-detail', kwargs={'slug': self.author.slug})

    def get_author_name(self):
        return self.author.username


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(News, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blog.title} - {self.user.username} - {self.id}"

    def get_absolute_url(self):
        return reverse('news-detail', kwargs={'slug': self.blog.slug})


class Comments(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    blog = models.ForeignKey(News, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.blog.title}"
