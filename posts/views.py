import datetime
import json

from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView

from el_pagination.views import AjaxListView

from .models import Post, Board
from .forms import PostForm

class FeedView(AjaxListView):
    model = Post
    context_object_name = "entry_list"
    template_name = "posts/feed.html"
    page_template = "posts/feed_posts.html"

    def dispatch(self, request, *args, **kwargs):
        self.board = None

        if "slug" in kwargs:
            self.board = get_object_or_404(Board, slug = self.kwargs["slug"])

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"board": self.board})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(approved = True).order_by("-pub_date")

        if self.board is not None:
            queryset = queryset.filter(board = self.board).order_by("-pub_date")

        return queryset

@login_required
@require_POST
def post(request, slug):
    board = get_object_or_404(Board, slug = slug)
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit = False)
        post.author = request.user
        post.board = board
        post.pub_date = timezone.now()
        post.save()

    return HttpResponseRedirect(reverse("posts:feed", args = (slug,)))

@login_required
@require_POST
def like(request):
    user = request.user
    post = get_object_or_404(Post, pk = request.POST["post_id"])
    liked = post.likes.filter(id = user.id).exists()

    if liked:
        post.likes.remove(user)
    else:
        post.likes.add(user)
    
    response = {"like_count": post.likes.count(), "liked": not liked}
    return HttpResponse(json.dumps(response), content_type = "application/json")