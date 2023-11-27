from rest_framework.routers import DefaultRouter

from server.apps.adviser.api.views import CategoryViewSet, LinkViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, 'categories')
router.register(r'links', LinkViewSet, 'links')
