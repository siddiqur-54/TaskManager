from django.contrib import admin
from django.urls import path

from accounts.views import (
    login_view,
    logout_view,
    register_view,
    update_view,
    change_password_view
)

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('register/', register_view, name='register_view'),
    path('update/', update_view, name='update_view'),
    path('change-password/', change_password_view, name='change_password_view'),
]