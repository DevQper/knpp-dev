from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, ProjectMediaViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'project-media', ProjectMediaViewSet, basename='project-media')

urlpatterns = [
    path('', include(router.urls)),
]

