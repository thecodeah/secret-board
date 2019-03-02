import datetime
import json

from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

from .models import Post, Like
from .forms import PostForm

class FeedView(generic.ListView):
    model = Post
    template_name = "posts/feed.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(approved = True).order_by("-pub_date")

@login_required
@require_POST
def post(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.pub_date = timezone.now()
        post.save()

    return HttpResponseRedirect(reverse("posts:feed"))

@login_required
@require_POST
def like(request):
    post = Post.objects.get(pk = request.POST["post_id"])
    new_like, created = Like.objects.get_or_create(user = request.user, post = post)
    if not created:
        new_like.delete()
    
    response = {"like_count": post.like_set.all().count()}
    return HttpResponse(json.dumps(response), content_type = "application/json")