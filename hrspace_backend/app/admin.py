from django.contrib import admin

from .models import (Application, Education, Expectations,
                     ExpectationsApplication, Experience, Language,
                     LanguageApplication, LanguageLevel, Occupation,
                     OccupationApplication, Payments, Registration,
                     RegistrationApplication, Salaryrecomend,
                     SalaryrecomendTown, Schedule, ScheduleApplication, Skill,
                     SkillApplication, SkillSpecialization, Specialization,
                     Towns)


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


@admin.register(SkillSpecialization)
class SkillSpecializationAdmin(admin.ModelAdmin):
    pass


@admin.register(Salaryrecomend)
class SalaryrecomendAdmin(admin.ModelAdmin):
    pass


@admin.register(SalaryrecomendTown)
class SalaryrecomendTownAdmin(admin.ModelAdmin):
    pass


class SkillApplicationInline(admin.TabularInline):
    model = SkillApplication


class LanguageApplicationInline(admin.TabularInline):
    model = LanguageApplication


class RegistrationApplicationInline(admin.TabularInline):
    model = RegistrationApplication


class OccupationApplicationInline(admin.TabularInline):
    model = OccupationApplication


class ScheduleApplicationInline(admin.TabularInline):
    model = ScheduleApplication


class ExpectationsApplicationInline(admin.TabularInline):
    model = ExpectationsApplication


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    inlines = [
        SkillApplicationInline,
        LanguageApplicationInline,
        RegistrationApplicationInline,
        OccupationApplicationInline,
        ScheduleApplicationInline,
        ExpectationsApplicationInline,
    ]
