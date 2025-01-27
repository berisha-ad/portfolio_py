from django.contrib import admin

from .models import project, backend_skill, frontend_skill, tool, file


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "date")


class SkillAdmin(admin.ModelAdmin):
    list_display = ("title", "iconlink")


class FileAdmin(admin.ModelAdmin):
    list_display = ("filename", "cvlink")


admin.site.register(project, PostAdmin)
admin.site.register(backend_skill, SkillAdmin)
admin.site.register(frontend_skill, SkillAdmin)
admin.site.register(tool, SkillAdmin)
admin.site.register(file, FileAdmin)
