from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (SpecializationViewSet,
                       ApplicationViewSet,
                       TownsViewSet,
                       SkillViewSet,
                       LanguageViewSet,
                       SalaryViewSet,
                       AllData)

v1_router = DefaultRouter()


v1_router.register(
    'app',  # поменять на app
    # r'spaces',
    ApplicationViewSet,
    basename='app')  # поменять на app


# v1_router.register(
#     'spaces/drafts',  # поменять на app
#     # r'spaces',
#     ApplicationViewSet,
#     basename='spaces')  # поменять на app

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

v1_router.register(
    'salary',
    SalaryViewSet,
    basename='salary')


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/spaces/', AllData.as_view(), name='my_endpoint'),
]
