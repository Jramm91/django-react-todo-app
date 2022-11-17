from django.contrib import admin
# import custom model
from .models import Task

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'due_date', 'completed')

# Register model


admin.site.register(Task, TaskAdmin)
