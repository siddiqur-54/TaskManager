from tasks.models import Task
from api.serializers import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def task_api_view(request, pk=None):
    task = None
    if request.method == 'GET':
        if pk is not None:
            try:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            task_list = Task.objects.all()
            serializer = TaskSerializer(task_list, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method in ['PUT', 'PATCH']:
        if pk is not None:
            try:
                task = Task.objects.get(pk=pk)
                serializer = TaskSerializer(task, data=request.data, partial=request.method == 'PATCH')
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not None:
            try:
                task = Task.objects.get(pk=pk)
                task.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            except Task.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)