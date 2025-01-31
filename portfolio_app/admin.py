from django.contrib import admin

from .models import Project, Backend_skill, Frontend_skill, Tool, File


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "iconlink")


class FileAdmin(admin.ModelAdmin):
    list_display = ("filename", "cvlink")


admin.site.register(Project, PostAdmin)
admin.site.register(Backend_skill, SkillAdmin)
admin.site.register(Frontend_skill, SkillAdmin)
admin.site.register(Tool, SkillAdmin)
admin.site.register(File, FileAdmin)
