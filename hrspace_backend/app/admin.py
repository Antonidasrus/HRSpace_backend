from django.contrib import admin

# from users.models import User
from .models import (
    Specialization,
    Towns,
    Experience,
    Education,
    Language,
    LanguageLevel,
    Registration,
    Occupation,
    Skill,
    Schedule,
    Expectations,
    Payments,
    Application,
    SkillApplication,
    LanguageApplication,
    ScheduleApplication,
    OccupationApplication,
    RegistrationApplication,
    ExpectationsApplication,
)


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Towns)
class TownsAdmin(admin.ModelAdmin):
    pass


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageLevel)
class LanguageLevelAdmin(admin.ModelAdmin):
    pass


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass


@admin.register(Occupation)
class OccupationAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    pass


@admin.register(Expectations)
class ExpectationsAdmin(admin.ModelAdmin):
    pass


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillApplication)
class SkillApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(LanguageApplication)
class LanguageApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(ScheduleApplication)
class ScheduleApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(OccupationApplication)
class OccupationApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(RegistrationApplication)
class RegistrationApplicationAdmin(admin.ModelAdmin):
    pass


@admin.register(ExpectationsApplication)
class ExpectationsApplicationAdmin(admin.ModelAdmin):
    pass
