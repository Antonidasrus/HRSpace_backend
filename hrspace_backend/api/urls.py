from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ApplicationViewSet, Application2ViewSet, Application3ViewSet

v1_router = DefaultRouter()
v1_router.register(
    'app',
    ApplicationViewSet,
    basename='app')
v1_router.register(
    'app2',
    Application2ViewSet,
    basename='app2'
)
v1_router.register(
    'app3',
    Application3ViewSet,
    basename='app3'
)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
