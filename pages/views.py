from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from .models import Project, MyInfo

class AboutMe(TemplateView):
    template_name = "about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_info'] = MyInfo.objects.all()[0]

        return context

def selected_works(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

def web_dev(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

def open_source(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

def game_dev(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

class Projects(TemplateView):
    template_name = "project_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = Project.objects.all()

        return context

# Create your views here.
