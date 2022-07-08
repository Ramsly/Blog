from django.contrib import admin

from .models import News, Favorite, Comments


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",), }


admin.site.register(Favorite)
admin.site.register(Comments)
