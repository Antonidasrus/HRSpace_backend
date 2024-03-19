from django.contrib import admin

from .models import Application, Skill, SkillApplication
# from users.models import User


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     pass


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    pass


# @admin.register(Profession)
# class ProfessionAdmin(admin.ModelAdmin):
#     pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(SkillApplication)
class SkillApplicationAdmin(admin.ModelAdmin):
    pass
