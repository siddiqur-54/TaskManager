from django.urls import path
from tasks.views import (
    task_create_view,
    task_delete_view,
    task_detail_view,
    task_list_search_completed_view,
    task_list_search_pending_view,
    task_update_view,
    mark_completed_view,
    mark_pending_view,
    task_image_delete_view,
)

app_name = 'tasks'

urlpatterns = [
    path('create/', task_create_view, name='task_create_view'),
    path('detail/<slug:slug>/', task_detail_view, name='task_detail_view'),
    path('update/<slug:slug>', task_update_view, name='task_update_view'),
    path('delete/<slug:slug>/', task_delete_view, name='task_delete_view'),
    path('list-search-pending/', task_list_search_pending_view, name='task_list_search_pending_view'),
    path('list-search-completed/', task_list_search_completed_view, name='task_list_search_completed_view'),
    path('mark-completed/<slug:slug>/', mark_completed_view, name='mark_completed_view'),
    path('mark-pending/<slug:slug>/', mark_pending_view, name='mark_pending_view'),
    path('delete-image/<int:image_id>/', task_image_delete_view, name='task_image_delete_view'),
]