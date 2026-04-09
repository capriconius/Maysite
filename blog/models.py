from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Rascunho'),
        ('published', 'Publicado'),
    )

    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True, null=True)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft'
    )
    created_on = models.DateTimeField(auto_now_add=True)   # data de criação
    updated_on = models.DateTimeField(auto_now=True)       # data de atualização

    def __str__(self):
        return self.title
