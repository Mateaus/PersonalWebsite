from django.contrib import admin
from .models import PostOverview, PostDetail, Tag

admin.site.register(Tag)

class PostDetailInline(admin.StackedInline):
    model = PostDetail

@admin.register(PostOverview)
class PostOverviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'estimated_time']
    filter_horizontal = ('tags',)
    inlines = [
        PostDetailInline
    ]