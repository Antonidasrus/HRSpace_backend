from django.contrib import admin

from .models import (Application, ApplicationCitizenship, ApplicationClaim,
                     ApplicationDuty, ApplicationOther, ApplicationProfession,
                     ApplicationSkill, Citizenship, Claim, Duty, Other,
                     Profession, Skill)


# Доработать админ зону поля
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'salary_min',
        'salary_max'
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationProfession)
class ApplicationProfessionAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'


@admin.register(Duty)
class DutyAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationDuty)
class ApplicationDutyAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationClaim)
class ApplicationClaimAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationSkill)
class ApplicationSkillAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'


@admin.register(Other)
class OtherAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationOther)
class ApplicationOtherAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'


@admin.register(Citizenship)
class CitizenshipAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
    )
    list_filter = ('name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


@admin.register(ApplicationCitizenship)
class ApplicationCitizenshipAdmin(admin.ModelAdmin):
    list_filter = ('application_id',)
    search_fields = ('application_id',)
    empty_value_display = '-пусто-'
