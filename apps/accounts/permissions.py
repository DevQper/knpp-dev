from django.contrib.auth import get_user_model
from rest_framework import permissions


class IsAdminRoleOrReadOnly(permissions.BasePermission):
    """
    Allows access to safe methods for everyone. Write operations require user role admin.
    """

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user = request.user
        if not user or not user.is_authenticated:
            return False

        User = get_user_model()
        return getattr(user, 'role', None) == User.Roles.ADMIN

