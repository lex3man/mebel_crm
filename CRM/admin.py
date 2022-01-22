from django.contrib import admin
from .models import Project, Tool, User, QType, Question, Wizard_step, Position, UserGroup, Inflow_base, Fund, Function, Status, Status_type

admin.site.register(Project)
admin.site.register(Position)
admin.site.register(Tool)
admin.site.register(User)
#admin.site.register(QType)
admin.site.register(Question)
admin.site.register(Wizard_step)
admin.site.register(UserGroup)
admin.site.register(Inflow_base)
admin.site.register(Fund)
admin.site.register(Function)
admin.site.register(Status)
admin.site.register(Status_type)