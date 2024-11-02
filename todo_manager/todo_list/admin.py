from todo_list.models import ToDoItem
from django.contrib import admin

@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    list_display = "id", "title", "done"
    list_display_links = "id", "title"
