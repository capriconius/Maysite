from django.urls import path
from blog.views import PostView, PostDetailView

urlpatterns = [
    path("", PostView.as_view(), name="home"),  # lista de posts publicados
    path("post/<slug:slug>/", PostDetailView.as_view(), name="post_detail"),  # detalhe do post
]

