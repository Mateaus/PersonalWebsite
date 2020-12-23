from django.contrib import admin
from .models import Post, PostDetail, Tag

admin.site.register(Tag)

class PostDetailInline(admin.StackedInline):
    model = PostDetail

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'estimated_time']
    filter_horizontal = ('tags',)
    inlines = [
        PostDetailInline
    ]