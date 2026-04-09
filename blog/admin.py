from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')  # mostra título e status na lista
    list_filter = ('status',)           # adiciona filtro por status
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}  # slug gerado a partir do título
