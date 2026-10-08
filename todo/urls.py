from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name="todo"),
    path('<int:id>', views.todoEdit, name='todoEdit'),
    path('add', views.todoAdd, name='todoAdd'),
    path('todo/<int:id>/done/', views.todoDone, name='todoDone'),
    path('todo/<int:id>/delete/', views.todoDelete, name='todoDelete')
]
