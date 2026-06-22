from .serializer import TaskSerializer
from .models import Task
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .filters import TaskFilter
from django_filters.rest_framework import DjangoFilterBackend

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter