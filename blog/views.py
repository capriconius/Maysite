from django.views.generic import ListView
from .models import Post

class PostView(ListView):
    model = Post
    template_name = "blog/home.html"
