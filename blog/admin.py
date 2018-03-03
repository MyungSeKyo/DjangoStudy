from django.contrib import admin
from blog.models import Post
from bookmark.models import Bookmark


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Post, PostAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
