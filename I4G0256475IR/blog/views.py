from I4G0256475IR.blog.models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ("__all__")
    success_url = reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post
    fields = ("__all__")
    success_url = reverse_lazy("blog:all")

class PostUpdateView(UpdateView):
    model = Post
    fields = ("__all__")
    success_url = reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = ("__all__")
    success_url = reverse_lazy("blog:all")