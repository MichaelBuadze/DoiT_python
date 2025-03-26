from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>', views.TaskDetail.as_view(), name = 'task'),
    path('task_create/>', views.TaskCreate.as_view(), name = 'task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),

]

# 127.0.0.1