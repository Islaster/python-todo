from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/create/', views.todoCreate.as_view(), name='todo_create'),
    path('todo/<int:todo_id>/', views.detail, name='detail'),
    path('todo/<int:pk>/delete/', views.todoDelete.as_view(), name='todo_delete'),
]