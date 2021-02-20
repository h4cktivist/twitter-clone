import datetime

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Post text')
    date = models.DateTimeField('Date')

    @property
    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))

    def __str__(self):
        return self.text


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Comment text')

    def __str__(self):
        return self.text
