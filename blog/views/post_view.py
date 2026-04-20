from django.views import generic
from blog.models import Post

class PostView(generic.ListView):
    # Filtra apenas posts com status=1 (publicado) e ordena por data de criação
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'posts'   # nome usado no template

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
