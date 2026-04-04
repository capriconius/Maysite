import pytest
from blog.factories import PostFactory

@pytest.mark.django_db
def test_create_post():
    post = PostFactory(title="Meu primeiro post")
    assert post.title == "Meu primeiro post"

@pytest.mark.django_db
def test_read_post():
    post = PostFactory()
    found = type(post).objects.get(id=post.id)
    assert found.title == post.title

@pytest.mark.django_db
def test_update_post():
    post = PostFactory()
    post.title = "Título atualizado"
    post.save()
    updated = type(post).objects.get(id=post.id)
    assert updated.title == "Título atualizado"

@pytest.mark.django_db
def test_delete_post():
    post = PostFactory()
    post_id = post.id
    post.delete()
    assert type(post).objects.filter(id=post_id).count() == 0
