from django.contrib import admin

# Register your models here.

from .models import Task, TaskList, Attachment  # Import additional models

# Register each model
admin.site.register(Task)
admin.site.register(TaskList)
admin.site.register(Attachment)
