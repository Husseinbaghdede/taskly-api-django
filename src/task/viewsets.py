from django.utils import timezone


from rest_framework import viewsets, mixins, response, filters
from .serializers import TaskListSerializer, TaskSerializer, AttachmentSerializer

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status as s
from rest_framework.decorators import action
from .models import Task, TaskList, Attachment, NOT_COMPLETE, COMPLETE
from .permissions import IsAllowedToEditTaskListElseNone, IsAllowedToEditAttachmentElseNone, IsAllowedToEditTaskElseNone


class TaskListViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      # mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone,]
    queryset = TaskList.objects.all()
    serializer_class = TaskListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAllowedToEditTaskListElseNone,]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name','status']
    filterset_fields = ['status', ]

    def get_queryset(self):
        query_set = super(TaskViewSet, self).get_queryset()
        user_profile = self.request.user.profile
        updated_queryset = query_set.filter(created_by=user_profile)
        return updated_queryset

    @action(detail=True, methods=['patch'])
    def update_task_status(self, request, pk=None):
        try:
            task = self.get_object()
            profile = request.user.profile
            status = request.data['status']
            if (status == NOT_COMPLETE):
                if (task.status == COMPLETE):
                    task.status = NOT_COMPLETE
                    task.completed_on = None
                    task.completed_by = None
                else:
                    raise Exception('Task is already marked as incomplete')
            elif (status == COMPLETE):
                if (task.status == NOT_COMPLETE):
                    task.status = COMPLETE
                    task.completed_on = timezone.now()
                    task.completed_by = profile
                else:
                    raise Exception('Task is already marked as complete')
            else:
                raise Exception('Incorrect status provided')
            task.save()
            serializer = TaskSerializer(
                instance=task, context={'request': request})
            return response.Response(serializer.data, status=s.HTTP_200_OK)
        except Exception as e:
            return response.Response({'detail': str(e)}, status=s.HTTP_400_BAD_REQUEST)


class AttachmentViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        # mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    permission_classes = [IsAllowedToEditAttachmentElseNone,]
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
