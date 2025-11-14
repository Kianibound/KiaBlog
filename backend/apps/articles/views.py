from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer
from .permissions import IsOwnerOrAdmin, IsWriterOrHigher  # Your custom
# ADD: Import UserRole separately (fixes attr)
from apps.users.models import User, UserRole


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related('author').prefetch_related(
        'tags', 'category')  # Base – optimize always
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated,
                          IsWriterOrHigher]  # Auth + role guard
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'category', 'tags__name']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwnerOrAdmin]
        else:
            permission_classes = [
                permissions.IsAuthenticatedOrReadOnly]  # Normals read
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        user = self.request.user
        # FIX: UserRole (imported class), not User.UserRole
        if user.role == UserRole.WRITER:
            return Article.objects.filter(author=user).select_related('author')
        return self.queryset  # All for admins (prefetched)

    @action(detail=False, methods=['get'])
    def drafts(self, request):
        drafts = self.get_queryset().filter(status='draft')
        serializer = self.get_serializer(drafts, many=True)
        return Response(serializer.data)
