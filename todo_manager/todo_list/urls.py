from django.urls import path, include
from . import views

app_name = "todo_list"

urlpatterns = [
    path('', views.ToDoListIndexView.as_view(), name="index"),
    path('<int:pk>/', views.ToDoDetailView.as_view(), name="detail"),
    path('list/', views.ToDoListView.as_view(), name="list"),
    path('done/', views.ToDoListDoneView.as_view(), name="done"),
]
