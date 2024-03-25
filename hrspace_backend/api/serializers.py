from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.models import (Application, Education, Expectations, Experience,
                        Language, LanguageApplication, LanguageLevel,
                        Occupation, Payments, Registration, Salaryrecomend,
                        Schedule, Skill, Specialization, Towns)

from app.validators import date_validator

class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = "__all__"


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class TownsSerializer(ModelSerializer):

    class Meta:
        model = Towns
        fields = "__all__"


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = ("name",)


class RegistrationSerializer(ModelSerializer):

    class Meta:
        model = Registration
        fields = ("name",)


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        fields = ("name",)


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("name",)


class ExpectationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expectations
        fields = ("name",)


class LanguageApplicationSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(queryset=Language.objects.all())
    language_level = serializers.CharField()

    class Meta:
        model = LanguageApplication
        fields = ("id", "language_level")


class ApplicationSerializer(ModelSerializer):
    specialization = serializers.CharField(source="specialization.name")
    experience = serializers.CharField(source="experience.name")
    education = serializers.CharField(source="education.name")
    payments = serializers.CharField(source="payments.name")
    towns = serializers.CharField(source="towns.name")

    date_employment = serializers.DateField(format="%d-%m-%Y")

    skills = serializers.SlugRelatedField(
        queryset=Skill.objects.all(), slug_field="name", many=True
    )
    registration = serializers.SlugRelatedField(
        queryset=Registration.objects.all(), slug_field="name", many=True
    )
    occupation = serializers.SlugRelatedField(
        queryset=Occupation.objects.all(), slug_field="name", many=True
    )
    timetable = serializers.SlugRelatedField(
        queryset=Schedule.objects.all(), slug_field="name", many=True
    )
    expectations = serializers.SlugRelatedField(
        queryset=Expectations.objects.all(), slug_field="name", many=True
    )

    languages = LanguageApplicationSerializer(required=False, many=True, source="language_list")

    def create(self, validated_data):
        specialization_name = validated_data.pop("specialization", {}).get("name")
        experience_name = validated_data.pop("experience", {}).get("name")
        education_name = validated_data.pop("education", {}).get("name")
        payments_name = validated_data.pop("payments", {}).get("name")
        towns_name = validated_data.pop("towns", {}).get("name")
        
        skills_data = validated_data.pop("skills", [])
        registration_data = validated_data.pop("registration", [])
        occupation_data = validated_data.pop("occupation", [])
        timetable_data = validated_data.pop("timetable", [])
        expectations_data = validated_data.pop("expectations", [])

        languages_data = validated_data.pop("language_list", [{}])

        specialization_instance, _ = Specialization.objects.get_or_create(
            name=specialization_name
        )
        experience_instance, _ = Experience.objects.get_or_create(name=experience_name)
        education_instance, _ = Education.objects.get_or_create(name=education_name)
        payments_instance, _ = Payments.objects.get_or_create(name=payments_name)
        towns_instance, _ = Towns.objects.get_or_create(name=towns_name)

        application = Application.objects.create(
            specialization=specialization_instance,
            experience=experience_instance,
            education=education_instance,
            payments=payments_instance,
            towns=towns_instance,
            **validated_data
        )

        application.skills.set(
            Skill.objects.filter(name__in=skills_data),
        )
        application.registration.set(
            Registration.objects.filter(name__in=registration_data)
        )
        application.occupation.set(Occupation.objects.filter(name__in=occupation_data))
        application.timetable.set(Schedule.objects.filter(name__in=timetable_data))
        application.expectations.set(
            Expectations.objects.filter(name__in=expectations_data)
        )

        language_application_list = []

        try:
            for language_data in languages_data:
                language_id = language_data["id"]
                language_level = language_data["language_level"]
                language_level, _ = LanguageLevel.objects.get_or_create(name=language_level)
                language_application_list.append(
                    LanguageApplication(
                        language_id=language_id,
                        application_id=application,
                        language_level=language_level,
                    )
                )
            LanguageApplication.objects.bulk_create(language_application_list)
        except KeyError:
            pass
        return application

    def validate(self, data):
        bonus = data['bonus']
        if bonus:
            try:
                if data['bonus_description'] in '':
                    raise serializers.ValidationError(
                        {'bonus_description': ['Неможет быть пустым.']}
                    )
            except KeyError:
                raise serializers.ValidationError(
                    {'bonus_description': ['Обязательное поле.']}
                )
        date_validator(data['date_employment'])
        return data

    def to_representation(self, instance):
        data = super().to_representation(instance)

        languages = instance.languages.all()
        languages_data = []

        for language in languages:
            language_data = LanguageSerializer(language).data
            language_application = LanguageApplication.objects.filter(
                application_id=instance.id, language_id=language.id
            ).first()
            if language_application:
                language_data["language_level"] = (
                    language_application.language_level.name
                )
            languages_data.append(language_data)

        data["languages"] = languages_data

        return data

    class Meta:
        model = Application
        fields = (
            "id",
            "employer_id",
            "date",
            "mission",
            "bonus",
            "bonus_description",
            "salary_min",
            "salary_max",
            "responsibilities",
            "other_requirements",
            "candidates_count",
            "recruiter_count",
            'date_employment',
            "award",
            "name",
            "specialization",
            "towns",
            "experience",
            "education",
            "payments",
            "skills",
            "languages",
            "registration",
            "occupation",
            "timetable",
            "expectations",
        )


class SalarySerializer(ModelSerializer):

    class Meta:
        model = Salaryrecomend
        fields = ("id", "salary_recomend")
