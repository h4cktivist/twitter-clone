import datetime
from PIL import Image

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Post text')
    image = models.ImageField('Image', upload_to='post_pics', blank=True)
    date = models.DateTimeField('Date')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked_by_user')

    @property
    def was_published_recently(self):
        return self.date >= (timezone.now() - datetime.timedelta(days=7))

    @property
    def likes(self):
        return self.liked.all().count()

    def save(self, *args, **kwargs):
        if self.image:
            super().save(*args, **kwargs)
            img = Image.open(self.image.path)

            if img.height > 500 or img.width > 500:
                img.thumbnail((500, 500))
                img.save(self.image.path)

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
