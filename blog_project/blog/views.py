from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import get_object_or_404


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/index.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    pk_url_kwarg = 'post_id'
