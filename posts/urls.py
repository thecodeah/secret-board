from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.FeedView.as_view(), name = "feed"),
    path('post', views.post, name = "post"),
    path('like', views.like, name = "like"),
]
