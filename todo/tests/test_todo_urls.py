from django.test import SimpleTestCase
from django.urls import reverse, resolve

from todo.views import TodoAddView, TodoListView, TodoMarkDoneView

__author__ = 'Shafikur Rahman Shaon'


class TestTodoUrls(SimpleTestCase):

    def test_todo_list_url_is_resolves(self):
        url = reverse('todo-list')
        self.assertEquals(resolve(url).func.view_class, TodoListView)

    def test_todo_add_url_is_resolves(self):
        url = reverse('todo-add')
        self.assertEquals(resolve(url).func.view_class, TodoAddView)

    def test_todo_mark_done_url_is_resolves(self):
        url = reverse('todo-mark-done', args=[1])
        self.assertEquals(resolve(url).func.view_class, TodoMarkDoneView)
