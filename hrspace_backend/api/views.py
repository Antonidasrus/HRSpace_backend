# from users.models import User
# from app_hr.models import Ingredient
from app.models import Application
from rest_framework.viewsets import ModelViewSet
# from .serializers import UserSerializer
from .serializers import ApplicationSerializer, Application2Serializer, Application3Serializer


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
