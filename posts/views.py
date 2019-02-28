import datetime

from django.shortcuts import render, reverse
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse

from .models import Post

class FeedView(generic.ListView):
    model = Post
    template_name = "posts/feed.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(approved = True).order_by("-pub_date")

def post(request):
    if request.method == "POST":
        post = Post()
        post.content = request.POST["content"]
        post.pub_date = datetime.datetime.now()
        post.save()

    return HttpResponseRedirect(reverse("posts:feed"))