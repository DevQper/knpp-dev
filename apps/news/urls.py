from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, NewsMediaViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'news-media', NewsMediaViewSet, basename='news-media')

urlpatterns = [
    path('', include(router.urls)),
]

