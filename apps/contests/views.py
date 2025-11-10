from rest_framework import viewsets
from .models import Contest
from .serializers import ContestSerializer, ContestCreateUpdateSerializer
from apps.accounts.permissions import IsAdminRoleOrReadOnly


class ContestViewSet(viewsets.ModelViewSet):
    queryset = Contest.objects.all()
    permission_classes = [IsAdminRoleOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ContestCreateUpdateSerializer
        return ContestSerializer
    
    def get_queryset(self):
        queryset = Contest.objects.all()
        return queryset.order_by('-created_at')
