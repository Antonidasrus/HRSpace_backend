# from users.models import User
# from app_hr.models import Ingredient
from rest_framework.viewsets import ModelViewSet

from app.models import Application
from app_hr.models import Application_hr

# from .serializers import UserSerializer
from .serializers import (Application2Serializer, Application3Serializer,
                          Application4Serializer, Application_hrSerializer,
                          ApplicationSerializer)

# class UserViewSet(ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class Application2ViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Application2Serializer


class Application3ViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Application3Serializer


class Application4ViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = Application4Serializer


class ApplicationHRViewSet(ModelViewSet):
    queryset = Application_hr.objects.all()
    serializer_class = Application_hrSerializer
