from app.models import Application, Specialization, Towns, Language, Skill
from rest_framework.viewsets import ModelViewSet
from .serializers import (ApplicationSerializer,
                          SpecializationSerializer,
                          TownsSerializer,
                          LanguageSerializer,
                          SkillSerializer,
                          SalarySerializer)
from .utils import istartswith_search


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class TownsViewSet(ModelViewSet):
    queryset = Towns.objects.all()
    serializer_class = TownsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get('specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(specialization__name=specialization_name)
        return istartswith_search(queryset, self)


class SalaryViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SalarySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get('specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(name=specialization_name)
        return queryset


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
