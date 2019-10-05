from django.urls import path

from . import views

app_name = "posts"
urlpatterns = [
    path('', views.FeedView.as_view(), name = "main_feed"),
    path('b/<slug:slug>/', views.FeedView.as_view(), name = "feed"),
    path('b/<slug:slug>/post', views.post, name = "post"),
    path('like', views.like, name = "like"),
    path('comment', views.comment, name = "comment"),
]
