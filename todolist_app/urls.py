from django.urls import path 
from todolist_app import views

urlpatterns = [
    path('', views.todolist , name = 'todolist'),
    path('delete/<task_id>', views.delete_task , name = 'delete'),
    path('edit/<task_id>', views.edit_task , name = 'edit'),
    path('mark-pending/<task_id>', views.mark_pending , name = 'pending'),
    path('mark-completed/<task_id>', views.mark_completed , name = 'completed'),
    
]
