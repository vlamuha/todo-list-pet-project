from django.urls import path

from task.views import (
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
]

app_name = "tasks"
