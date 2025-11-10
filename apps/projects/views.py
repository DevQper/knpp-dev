from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from .models import Project, ProjectMedia
from .serializers import ProjectSerializer, ProjectCreateUpdateSerializer, ProjectMediaSerializer


class ProjectPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    pagination_class = ProjectPagination
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProjectCreateUpdateSerializer
        return ProjectSerializer
    
    def get_queryset(self):
        queryset = Project.objects.all()
        return queryset.order_by('-created_at')


class ProjectMediaViewSet(viewsets.ModelViewSet):
    queryset = ProjectMedia.objects.all()
    serializer_class = ProjectMediaSerializer
    parser_classes = [MultiPartParser, FormParser]
    
    def get_queryset(self):
        queryset = ProjectMedia.objects.all()
        project_id = self.request.query_params.get('project_id', None)
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
        return queryset
