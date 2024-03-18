from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ApplicationViewSet

v1_router = DefaultRouter()
v1_router.register(
    'app',
    ApplicationViewSet,
    basename='app')


urlpatterns = [
    path('v1/spaces/', include(v1_router.urls)),
]
