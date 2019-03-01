import datetime

from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone

from .models import Post
from .forms import PostForm

class FeedView(generic.ListView):
    model = Post
    template_name = "posts/feed.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(approved = True).order_by("-pub_date")

def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()

    return HttpResponseRedirect(reverse("posts:feed"))