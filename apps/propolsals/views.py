from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Proposal
from .serializers import ProposalSerializer, ProposalCreateUpdateSerializer
from apps.accounts.permissions import IsAdminRoleOrReadOnly


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdminRoleOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProposalCreateUpdateSerializer
        return ProposalSerializer
    
    def get_queryset(self):
        queryset = Proposal.objects.all()
        return queryset.order_by('-created_at')
