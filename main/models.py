import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Post text')
    date = models.DateTimeField('Date')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked_by_user')

    @property
    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))

    @property
    def likes(self):
        return self.liked.all().count()

    def __str__(self):
        return self.text


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike')
)

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked_user')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    value = models.CharField(max_length=10, choices=LIKE_CHOICES, default='Like')

    def __str__(self):
        return self.value


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.CharField('User', max_length=100)
    text = models.TextField('Comment text')

    def __str__(self):
        return self.text
