from django.views.generic import ListView
from .models import Post

class PostView(ListView):
    model = Post
    template_name = "blog/home.html"

    def get_queryset(self):
        # Filtra apenas os posts publicados
        return Post.objects.filter(status="publicado")
