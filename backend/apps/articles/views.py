from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Article
from .serializers import ArticleSerializer


# Full CRUD: List/Create/Retrieve/Update/Destroy
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all().select_related() # Efficient: No extra queries
    serializer_class = ArticleSerializer
    filter_backends = [DjangoFilterBackend]  # For ?status=published
    filterset_fields = ['status']  # Queryable – scales to prod

    # Custom: /articles/drafts/ – bonus for interviews
    @action(detail=False, methods=['get'])
    def drafts(self, request):
        drafts = self.get_queryset().filter(status='draft')
        serializer = self.get_serializer(drafts, many=True)
        return Response(serializer.data)
