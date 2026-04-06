import pytest
import factory
from faker import Factory as FakerFactory

from django.contrib.auth.models import User
from django.utils.timezone import now

from blog.models import Post

faker = FakerFactory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())

    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class PostFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    created_on = factory.LazyAttribute(lambda x: now())
    author = factory.SubFactory(UserFactory)
    status = 0

    class Meta:
        model = Post


# ------------------------
# Testes CRUD com pytest
# ------------------------

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

