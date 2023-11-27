from django.urls import path, include

from server.apps.adviser.api.routers import router as adviser_router
from server.apps.user.api.routers import router as user_router


urlpatterns = [
    path(r'adviser/', include(adviser_router.urls)),
    path(r'users/', include(user_router.urls))
]
