from rest_framework.serializers import ModelSerializer
# from rest_framework import serializers

from app.models import Application, Specialization, Towns, Skill, Language


class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class TownsSerializer(ModelSerializer):

    class Meta:
        model = Towns
        fields = '__all__'


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'


class SalarySerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = ('id', 'salary_recomend')
