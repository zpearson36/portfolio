from django.contrib import admin

from .models import Project
from .models import MyInfo
from .models import MyWork
from .models import WorkProject

admin.site.register(Project)
admin.site.register(MyInfo)
admin.site.register(MyWork)
admin.site.register(WorkProject)
