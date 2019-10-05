from django.contrib import admin

from .models import Post, Board, Comment

admin.site.register(Post)
admin.site.register(Board)
admin.site.register(Comment)
