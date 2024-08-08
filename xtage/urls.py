from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from app.views import (
    BookViewSet,
    BookRecommendationViewSet,
    CommentViewSet,
    LikeViewSet,
    search_books
)

# Set up the router
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'recommendations', BookRecommendationViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likes', LikeViewSet)

# Set up Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Book API",
        default_version='v1',
        description="API for managing book recommendations",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Define URL patterns
urlpatterns = [
    path('', include(router.urls)),
    path('api/search/', search_books, name='search-books'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
