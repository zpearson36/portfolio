from django import template

from pages.models import Project, MyInfo

register = template.Library()

@register.simple_tag
def get_dropdown_projects():
    return Project.objects.all()[:3]

@register.simple_tag
def get_my_info():
    return MyInfo.objects.all()[0]
