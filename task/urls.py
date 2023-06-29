from django.urls import path

from task.views import IndexView, TagListView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
]

app_name = "tasks"
