from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, FormView, TemplateView

from .forms import ContactForm
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

class ProjectDetail(DetailView):
    template_name = "project_detail.html"
    model = Project
    context_object_name = "project"

class ContactMe(FormView):
    template_name = "contact_me.html"
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_info'] = MyInfo.objects.all()[0]

        return context

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_invalid(self, form):
        messages.add_message(self.request, messages.WARNING, "Message Unsuccessful")

        for field in form.errors:
            form[field].field.widget.attrs['class'] += ' alert alert-danger'
        return super().form_invalid(form)

    def form_valid(self, form):
        form.send_email()
        messages.add_message(self.request, messages.SUCCESS, "Message Sent Successfully")
        return super().form_valid(form)


# Create your views here.
