from django import forms
from django.forms import ModelForm

from todo.models import Todo

__author__ = 'Shafikur Rahman Shaon'


class TodoForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input'})
    )

    class Meta:
        model = Todo
        fields = ('title',)
