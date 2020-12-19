from django.views.generic.base import TemplateView
from .models import PostOverview, PostDetail

class BlogView(TemplateView):
    template_name = "blog/blog.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_overviews'] = PostOverview.objects.all()
        return context

class PostView(TemplateView):
    template_name = "blog/blog_post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_detail'] = PostDetail.objects.get(pk=context['pk'])
        return context