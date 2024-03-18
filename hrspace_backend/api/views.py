from app.models import Application
from rest_framework.viewsets import ModelViewSet
from .serializers import ApplicationSerializer


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
