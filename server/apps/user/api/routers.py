from rest_framework.routers import DefaultRouter

from server.apps.user.api.views import UserViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, 'users')
