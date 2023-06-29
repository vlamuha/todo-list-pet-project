from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from task.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = 'task/index.html'
    context_object_name = "task_list"
    paginate_by = 5

    def post(self, request):
        pk = request.POST.get('pk')

        task = Task.objects.get(id=pk)
        if task.is_completed:
            task.is_completed = False
        else:
            task.is_completed = True
        task.save()

        return HttpResponseRedirect(self.request.path)


class TagListView(generic.ListView):
    model = Tag
    template_name = "task/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    template_name = "task/tag_form.html"
    success_url = reverse_lazy("tasks:index")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "task/tag_form.html"


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")
    template_name = "task/tag_confirm_delete.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task/task_form.html"
    success_url = reverse_lazy("tasks:index")


