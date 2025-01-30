from django.shortcuts import render
from .models import project, backend_skill, frontend_skill, tool, file


def index(request):
    backend = backend_skill.objects.all()
    frontend = frontend_skill.objects.all()
    tools = tool.objects.all()
    cv = file.objects.all()
    return render(request, "portfolio/index.html", {
        "backend": backend,
        "frontend": frontend,
        "tools": tools,
        "file": cv
    })


def projects(request):
    projects = project.objects.all()

    for sinproject in projects:
        sinproject.skills_list = [
            skill.strip() for skill in sinproject.skills.split(",") if skill.strip()]

    return render(request, "portfolio/projects.html", {
        "projects": projects
    })


def imprint(request):
    files = file.objects.first()
    return render(request, "portfolio/imprint.html", {
        "files": files
    })
