from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, FormParser
from .models import News, NewsMedia
from .serializers import NewsSerializer, NewsCreateUpdateSerializer, NewsMediaSerializer
from apps.accounts.permissions import IsAdminRoleOrReadOnly


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    permission_classes = [IsAdminRoleOrReadOnly]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return NewsCreateUpdateSerializer
        return NewsSerializer
    
    def get_queryset(self):
        queryset = News.objects.all()
        return queryset.order_by('-created_at')


class NewsMediaViewSet(viewsets.ModelViewSet):
    queryset = NewsMedia.objects.all()
    serializer_class = NewsMediaSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [IsAdminRoleOrReadOnly]
    
    def get_queryset(self):
        queryset = NewsMedia.objects.all()
        news_id = self.request.query_params.get('news_id', None)
        if news_id is not None:
            queryset = queryset.filter(news_id=news_id)
        return queryset
