from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (Application2ViewSet, Application3ViewSet,
                       Application4ViewSet, ApplicationHRViewSet,
                       ApplicationViewSet)

v1_router = DefaultRouter()
v1_router.register("app", ApplicationViewSet, basename="app")
v1_router.register("app2", Application2ViewSet, basename="app2")
v1_router.register("app3", Application3ViewSet, basename="app3")
v1_router.register(
    r"app4/(?P<application_id>\d+)", Application4ViewSet, basename="app4"
)
v1_router.register("app_hr", ApplicationHRViewSet, basename="app_hr")

urlpatterns = [
    path("v1/", include(v1_router.urls)),
]
