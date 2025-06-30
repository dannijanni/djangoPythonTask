from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Tasks, Projects, Users
from core.serializers.task_serializer import TaskCreateSerializer, TaskSerializer
from django.shortcuts import get_object_or_404

class CreateTask(APIView):
    def post(self, request):
        # Map frontend keys (both camelCase and snake_case) to serializer field names
        data = request.data.copy()
        # Project mapping
        if 'projectId' in data:
            data['project'] = data.pop('projectId')
        elif 'project_id' in data:
            data['project'] = data.pop('project_id')
        # Created_by mapping
        if 'createdBy' in data:
            data['created_by'] = data.pop('createdBy')
        elif 'created_by' in data:
            data['created_by'] = data.get('created_by')
        # AssignedTo maps to closed_by
        if 'assignedTo' in data:
            data['closed_by'] = data.pop('assignedTo')
        elif 'closed_by' in data:
            data['closed_by'] = data.get('closed_by')
        # due_date mapping
        if 'dueDate' in data:
            data['due_date'] = data.pop('dueDate')
        elif 'due_date' in data:
            data['due_date'] = data.get('due_date')

        # Normalize priority
        if 'priority' in data:
            data['priority'] = data['priority'].capitalize()
        # Normalize status
        if 'status' in data:
            status_map = {
                'To Do': 'Open',
                'In Progress': 'In Progress',
                'Done': 'Closed',
                'Open': 'Open',
                'Closed': 'Closed'
            }
            data['status'] = status_map.get(data['status'], data['status'])

        print("🔥 Mapped data:", data)
        serializer = TaskCreateSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        print("❌ Serializer Errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetAllTasks(APIView):
    def get(self, request):
        print("🔄 Mapped update data:", request.data)
        tasks = Tasks.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GetTaskById(APIView):
    def get(self, request, task_id):
        print("🔄 Mapped update data:", request.data)
        task = get_object_or_404(Tasks, id=task_id)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UpdateTaskById(APIView):
    def put(self, request, task_id):
        
        task = Tasks.objects.filter(id=task_id).first()
        if not task:
            return Response({"detail": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        # Map frontend keys
        if 'projectId' in data:
            data['project_id'] = data.pop('projectId')
        if 'createdBy' in data:
            data['created_by'] = data.pop('createdBy')
        if 'assignedTo' in data:
            data['closed_by'] = data.pop('assignedTo')
        if 'dueDate' in data:
            data['due_date'] = data.pop('dueDate')
        # Normalize priority and status to match DB enum values
        if 'priority' in data:
            # e.g., 'low' -> 'Low'
            data['priority'] = data['priority'].capitalize()
        if 'status' in data:
            # Map frontend status labels to enum values
            status_map = {
                'To Do': 'Open',
                'In Progress': 'In Progress',
                'Done': 'Closed',
                'Open': 'Open',
                'Closed': 'Closed'
            }
            data['status'] = status_map.get(data['status'], data['status'])

        print("🔄 Mapped update data:", data)
        serializer = TaskCreateSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        print("❌ Serializer Errors (update):", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskById(APIView):
    def delete(self, request, task_id):
        task = get_object_or_404(Tasks, id=task_id)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)