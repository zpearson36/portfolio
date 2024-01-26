from django.urls import path

from . import views

urlpatterns = [
        path("",                            views.AboutMe.as_view(),       name="index"),
        path("projects",                    views.Projects.as_view(),      name="projects"),
        path("project_detail/<int:pk>",     views.ProjectDetail.as_view(), name="project_detail"),
        path("contact_me",                  views.ContactMe.as_view(),     name="contact_me"),
        path("work_list",                   views.WorkList.as_view(),      name="work_list"),
        path("work_projects/<int:work_pk>", views.WorkProjects.as_view(),  name="work_projects"),
        ]
