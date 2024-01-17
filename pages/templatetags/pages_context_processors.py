from django import template

from pages.models import Project

register = template.Library()

@register.simple_tag
def get_dropdown_projects():
    return Project.objects.all()[:3]
