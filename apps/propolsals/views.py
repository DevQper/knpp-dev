from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Proposal
from .serializers import ProposalSerializer, ProposalCreateUpdateSerializer
from .filters import ProposalFilter


class ProposalPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer
    parser_classes = [MultiPartParser, FormParser]
    pagination_class = ProposalPagination
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProposalFilter
    search_fields = ['title', 'description', 'proposed_by', 'email']
    ordering_fields = ['created_at', 'updated_at', 'status', 'type', 'title']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ProposalCreateUpdateSerializer
        return ProposalSerializer
