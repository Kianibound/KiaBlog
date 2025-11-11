from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
# /articles/ for list, /articles/1/ for detail
router.register(r'articles', ArticleViewSet, basename='article')

urlpatterns = router.urls
