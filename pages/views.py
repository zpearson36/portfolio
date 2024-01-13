from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template("landing_page.html")
    return HttpResponse(template.render())

def about_me(request):
    template = loader.get_template("about_me.html")
    return HttpResponse(template.render())
# Create your views here.
