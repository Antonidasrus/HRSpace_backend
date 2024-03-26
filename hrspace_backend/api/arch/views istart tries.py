from rest_framework.viewsets import ModelViewSet

from app.models import Application, Specialization

from .serializers import ApplicationSerializer, SpecializationSerializer

# def startswith_search(queryset, self):
#     """
#     Поиск по частичному вхождению
#     в начале названия.
#     """
#     name = self.request.query_params.get('name')
#     if name:
#         queryset = queryset.filter(name__istartswith=name)
#     return queryset


class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__istartswith=name)
        return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return startswith_search(queryset, self)


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     towns = self.request.query_params.get('towns')
    #     specialization_name = self.request.query_params.get('specialization_name')
    #     if towns:
    #         queryset = queryset.filter(towns__name__istartswith=towns)
    #     if specialization_name:
    #         queryset = queryset.filter(specialization__name__istartswith=specialization_name)
    #     return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     towns = self.request.query_params.get('towns')
    #     if towns:
    #         queryset = queryset.filter(towns__name__istartswith=towns)
    #     return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     towns_name = self.request.query_params.get('towns_name')
    #     if towns_name:
    #         queryset = queryset.filter(towns__name__istartswith=towns_name)
    #     return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     specialization_name = self.request.query_params.get('specialization_name')
    #     if specialization_name:
    #         queryset = queryset.filter(specialization__name__istartswith=specialization_name)
    #     return queryset

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return startswith_search(queryset, self)
