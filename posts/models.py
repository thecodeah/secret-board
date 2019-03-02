from django.conf import settings
from django.db import models

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, default = 1)
    content = models.CharField(max_length = 280)
    pub_date = models.DateTimeField()
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return self.content

class Like(models.Model):
    post = models.ForeignKey(Post, models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE)
