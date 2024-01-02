from django.contrib import admin
from .models import Task, TaskImage

class TaskImageInline(admin.TabularInline):
    model = TaskImage
    extra = 1

class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'slug']
    search_fields = ['user', 'title', 'priority', 'deadline', 'pending']
    inlines = [TaskImageInline]

class TaskImageAdmin(admin.ModelAdmin):
    list_display = ['task', 'image']

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskImage, TaskImageAdmin)
