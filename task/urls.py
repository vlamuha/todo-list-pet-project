from django.urls import path

from task.views import IndexView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]

app_name = "tasks"
