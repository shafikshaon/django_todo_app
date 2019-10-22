from django.urls import path

from todo.views import TodoAddView, TodoListView, TodoMarkDoneView

__author__ = 'Shafikur Rahman Shaon'

urlpatterns = [
    path('', TodoListView.as_view(), name='todo-list'),
    path('add/', TodoAddView.as_view(), name='todo-add'),
    path('mark-done/<pk>', TodoMarkDoneView.as_view(), name='todo-mark-done'),
]
