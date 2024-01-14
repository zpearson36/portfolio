from django.http import HttpResponse
from django.template import loader

def about_me(request):
    template = loader.get_template("about_me.html")
    return HttpResponse(template.render())

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

def projects(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

# Create your views here.
