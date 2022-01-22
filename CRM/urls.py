from django.urls import path
from . import views
from .views import web_hook, main_data

urlpatterns = [
    path('', views.index, name = 'index'),
    path('new_project/', views.add_proj, name = 'add_proj'),
    path('sets_api/', web_hook.as_view()),
    path('main_data/', main_data.as_view()),
]