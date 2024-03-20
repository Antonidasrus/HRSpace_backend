from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import ApplicationViewSet

v1_router = DefaultRouter()
v1_router.register(
    'spaces', # поменять на app
    ApplicationViewSet,
    basename='spaces') # поменять на app


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
