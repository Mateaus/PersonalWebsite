from django.contrib import admin
from .models import Post, Potato, Root, Tag

admin.site.register(Tag)

@admin.register(Post)
class PostOverviewAdmin(admin.ModelAdmin):
    list_display = ['title', 'estimated_time']
    filter_horizontal = ('tags',)


class RootInline(admin.StackedInline):
    model = Root

@admin.register(Potato)
class PotatoAdmin(admin.ModelAdmin):
    inlines = [
        RootInline
    ]

