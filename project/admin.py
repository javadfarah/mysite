from django.contrib import admin
from project.models import Post
# Register your models here.
from project.models import Post, PostFile

class FeedFileInline(admin.TabularInline):
    model = PostFile


class FeedAdmin(admin.ModelAdmin):
    inlines = [
        FeedFileInline,
    ]

admin.site.register(Post, FeedAdmin)

