from django.contrib import admin
from .models import Project, Skill, Experience

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    search_fields = ('title', 'summary', 'description')
    list_filter = ('category', 'created_at')
    ordering = ('-created_at',)

class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    search_fields = ('name', 'category')
    list_filter = ('category', 'proficiency')

class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'start_date', 'is_current')
    search_fields = ('title', 'company', 'description')
    list_filter = ('is_current', 'start_date')
    ordering = ('-start_date',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
