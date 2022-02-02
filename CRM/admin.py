from django.contrib import admin
from .models import Project, Tool, User, Question, Wizard_step, Position, UserGroup, Inflow_base, Fund, Function, Status, Status_type, Resources_type, Resource, Bot_config, Client_contact

admin.site.register(Project)
admin.site.register(Position)
admin.site.register(Tool)
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Wizard_step)
admin.site.register(UserGroup)
admin.site.register(Inflow_base)
admin.site.register(Fund)
admin.site.register(Function)
admin.site.register(Status)
admin.site.register(Status_type)
admin.site.register(Resources_type)
admin.site.register(Resource)
admin.site.register(Bot_config)
admin.site.register(Client_contact)