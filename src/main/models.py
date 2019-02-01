from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify


class DateData(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True


class User(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class Title(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class Content(models.Model):
    content = models.TextField()

    class Meta:
        abstract = True


class Tagged(models.Model):
    tags = models.ManyToManyField('Tag', blank=True)

    class Meta:
        abstract = True


class Voted(models.Model):
    up_votes = models.IntegerField()
    down_votes = models.IntegerField()

    class Meta:
        abstract = True


class IP(models.Model):
    ip_address = models.GenericIPAddressField(blank=True, db_index=True)

    class Meta:
        abstract = True


class Tag(models.Model):
    slug = models.SlugField(allow_unicode=True)

    def get_absolute_url(self):
        return reverse_lazy("tagged", args=(self.slug,), current_app="main")


class Category(Title, Content, DateData):
    slug = models.SlugField(unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return reverse_lazy("category", args=(self.slug,), current_app="main")


class Question(User, IP, Title, Content, Tagged, Voted, DateData):
    category = models.ForeignKey("Category")
    closed = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=200, allow_unicode=True)

    def get_absolute_url(self):
        return reverse_lazy("question_details", args=(self.slug,), current_app="main")


class Answer(User, IP, Title, Content, Tagged, Voted, DateData):
    accepted = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.PROTECT)


class Comment(User, IP, Content, Voted, DateData):
    question = models.ForeignKey(
        'Question', blank=True, on_delete=models.PROTECT)
    answer = models.ForeignKey('Answer', blank=True, on_delete=models.PROTECT)
    comment = models.ForeignKey(
        'Comment', blank=True, on_delete=models.PROTECT)
