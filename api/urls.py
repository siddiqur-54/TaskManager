from django.urls import path
from api.views import (
    task_api_view
)

app_name = 'api'

urlpatterns = [
    path('task-view/', task_api_view, name="task_all_api_view"),
    path('task-view/<int:pk>/', task_api_view, name="task_single_api_view"),
]