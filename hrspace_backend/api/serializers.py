from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers

from app.models import Application, Specialization


class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
