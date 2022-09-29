from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class WikiTopic(models.Model):
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.CharField(max_length=255, null=True)
    category = models.CharField(max_length=200, null=True)  # TODO: add new table for categories
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name


class WikiSection(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    topic = models.ForeignKey(WikiTopic, on_delete=models.CASCADE, related_name='sections')
    views = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'topic',)

    def __str__(self):
        name = [self.topic.name, self.title]
        s = "-"
        return s.join(name)


class WikiContent(models.Model):
    section = models.ForeignKey(WikiSection, on_delete=models.CASCADE, related_name='pages')
    dom = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)


class WikiLike(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE)
    likee = models.ForeignKey(WikiSection, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)


class WikiFollow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower_user')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following_user')
    created = models.DateTimeField(auto_now_add=True)
