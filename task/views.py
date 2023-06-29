from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic

from task.models import Task


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
