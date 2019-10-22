from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=128, null=False)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        app_label = 'todo'
        ordering = ('-status', '-created',)
