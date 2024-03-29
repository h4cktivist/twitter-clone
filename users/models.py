from django.db import models
from django.contrib.auth.models import User

from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile_pics/default.jpg', upload_to='profile_pics')
    bio = models.TextField(default='Apparently, this user prefers to keep an air of mystery about them.')
    bg_image = models.ImageField(default='bg_pics/default.jpg', upload_to='bg_pics')
    following = models.ManyToManyField(User, related_name='following', blank=True)

    @property
    def following_count(self):
        return self.following.all().count()

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            new_size = (300, 300)
            img.thumbnail(new_size)
            img.save(self.image.path)
