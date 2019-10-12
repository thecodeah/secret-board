from django.conf import settings
from django.db import models

class Board(models.Model):
    slug = models.SlugField()

    def __str__(self):
        return self.slug

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, default = 1)
    content = models.CharField(max_length = 280)
    board = models.ForeignKey(Board, models.SET_NULL, null = True)
    pub_date = models.DateTimeField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "likes")
    hidden = models.BooleanField(default = False)
    popularity = models.IntegerField(default = 3)

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, default = 1)
    content = models.CharField(max_length = 280)
    post = models.ForeignKey(Post, models.CASCADE)
    pub_date = models.DateTimeField()

    class Meta():
        ordering = ['pub_date']
    
    def __str__(self):
        return self.content
