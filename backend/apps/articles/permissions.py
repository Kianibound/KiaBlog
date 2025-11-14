from rest_framework import permissions
from apps.users.models import User, UserRole  # ADD: Import UserRole

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.role in [UserRole.ADMIN, UserRole.SUPERADMIN]:  # FIX: UserRole (class), not User.UserRole
            return True
        if user.role == UserRole.WRITER:
            return obj.author == user
        return False

class IsWriterOrHigher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role in [UserRole.WRITER, UserRole.ADMIN, UserRole.SUPERADMIN]  # FIX + null check (edge: anon)