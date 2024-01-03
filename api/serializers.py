from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'id',
            'user',
            'title',
            'description',
            'priority',
            'deadline',
            'created_at',
            'updated_at',
            'pending',
            'slug'
        ]