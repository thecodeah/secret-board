from django.db import models

class Post(models.Model):
    content = models.CharField(max_length = 280)
    pub_date = models.DateTimeField()
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    approved = models.BooleanField(default = False)

    def __str__(self):
        return self.content