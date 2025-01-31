from django.shortcuts import render
from .models import Project, Backend_skill, Frontend_skill, Tool, File


def index(request):
    backend = Backend_skill.objects.all()
    frontend = Frontend_skill.objects.all()
    tools = Tool.objects.all()
    cv = File.objects.all()
    return render(request, "portfolio/index.html", {
        "backend": backend,
        "frontend": frontend,
        "tools": tools,
        "file": cv
    })


def projects(request):
    projects = Project.objects.all().order_by('sort_order')
    cv = File.objects.all()

    for sinproject in projects:
        sinproject.skills_list = [
            skill.strip() for skill in sinproject.skills.split(",") if skill.strip()]

    return render(request, "portfolio/projects.html", {
        "projects": projects,
        "file": cv
    })


def imprint(request):
    cv = File.objects.all()
    return render(request, "portfolio/imprint.html", {
        "file": cv
    })
