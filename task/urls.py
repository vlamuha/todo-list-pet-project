from django.urls import path

from task.views import (
    IndexView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
)

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("tasks/create/", TaskCreateView.as_view(), name="task-create"),
    path("tasks/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
]

app_name = "tasks"
