from django.urls import path

from . import views

urlpatterns = [
        path("",                        views.AboutMe.as_view(),       name="index"),
        path("selected_works",          views.selected_works,          name="selected_works"),
        path("web_dev",                 views.web_dev,                 name="web_dev"),
        path("open_source",             views.open_source,             name="open_source"),
        path("game_dev",                views.game_dev,                name="game_dev"),
        path("projects",                views.Projects.as_view(),      name="projects"),
        path("project_detail/<int:pk>", views.ProjectDetail.as_view(), name="project_detail"),
        path("contact_me",              views.ContactMe.as_view(),     name="contact_me"),
        ]
