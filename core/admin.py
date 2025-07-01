from django.contrib import admin

from .models import Projects, Roles, Tasks, Users

admin.site.register(Projects)
admin.site.register(Roles)
admin.site.register(Tasks)
admin.site.register(Users)

# Register your models here.
