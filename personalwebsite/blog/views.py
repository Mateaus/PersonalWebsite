from django.views.generic.base import TemplateView
from .models import Post, PostDetail

class PostListView(TemplateView):
    template_name = "blog/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

class PostDetailView(TemplateView):
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_detail'] = PostDetail.objects.get(pk=context['pk'])
        return context