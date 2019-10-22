from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from todo.forms import TodoForm
from todo.models import Todo


class TodoAddView(CreateView):
    template_name = 'todo/add.html'
    form_class = TodoForm

    def get(self, request, *args, **kwargs):
        return super(TodoAddView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        todo = form.save(commit=False)
        todo.save()
        return HttpResponseRedirect(reverse('todo-list'))


class TodoListView(ListView):
    template_name = 'todo/list.html'
    model = Todo
    context_object_name = 'objects_list'

    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        context['total_active'] = self.model.objects.filter(status=True).count()
        context['total_inactive'] = self.model.objects.filter(status=False).count()
        return context


class TodoMarkDoneView(DeleteView):
    model = Todo
    success_url = reverse_lazy('todo-list')

    def get(self, request, *args, **kwargs):
        todo = super(TodoMarkDoneView, self).get(request, *args, **kwargs)
        todo = self.get_object()
        if not todo.status:
            # The todo has been deleted if todo already mark as done
            todo.delete()
            return HttpResponseRedirect(reverse('todo-list'))
        todo.status = False
        todo.save()
        return HttpResponseRedirect(reverse('todo-list'))
