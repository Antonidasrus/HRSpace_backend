from users.models import User
# from app_hr.models import Ingredient
# from app.models import Ingredient
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
