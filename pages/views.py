from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.views.generic import DetailView, FormView, ListView, TemplateView

from .forms import ContactForm
from .models import Project, MyInfo, MyWork, WorkProject 

class AboutMe(TemplateView):
    template_name = "about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_info'] = MyInfo.objects.all()[0]

        return context

class ContactMe(FormView):
    template_name = "contact_me.html"
    form_class = ContactForm
    success_url = "contact_me"

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

class WorkList(ListView):
    template_name = "work_list.html"
    model = MyWork

class WorkProjects(ListView):
    template_name = "work_detail.html"
    model = WorkProject

    def dispatch(self, request, *args, **kwargs):
        self.work_pk = kwargs['work_pk']

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = self.model.objects.filter(job_foreign_key=self.work_pk)

        return context
