from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (ApplicationViewSet,
                       SpecializationViewSet,
                       TownsViewSet,
                       SkillViewSet,
                       LanguageViewSet)

v1_router = DefaultRouter()
v1_router.register(
    'spaces', # поменять на app
    ApplicationViewSet,
    basename='spaces') # поменять на app

# для тестов. проверить, будет ли на фронте без урла работать istartswith
v1_router.register(
    'specializations',
    SpecializationViewSet,
    basename='specializations')

v1_router.register(
    'towns',
    TownsViewSet,
    basename='towns')

v1_router.register(
    'skill',
    SkillViewSet,
    basename='skill')

v1_router.register(
    'language',
    LanguageViewSet,
    basename='language')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
